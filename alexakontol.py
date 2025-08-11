from telethon import TelegramClient, events
import asyncio
import random
from random import randint
from time import sleep


###############INPUT PART###############

api_id = '28119255'
api_hash = '337f330b7ab0c169c6296bc80338c6fd'
phone = '+6283185102534'
messages = ["test1", "test2","test3"]

client = TelegramClient('anon', api_id, api_hash)

###############INPUT PART###############

async def my_event_handler(event):
    chat_id = event.chat_id

    if "new" in event.text.lower():
            await asyncio.sleep(random.randint(10,20))
            message_content = random.choice(messages)
            await client.send_message(chat_id, message_content)       
  
    elif "start" in event.text.lower():
        reply_message = "test"
        await event.reply(reply_message)

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input('Enter the code: ')
        await client.sign_in(phone, code)

    client.add_event_handler(my_event_handler, events.NewMessage)
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
















