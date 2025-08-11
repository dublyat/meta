from telethon import TelegramClient, events
import asyncio
import random
from random import randint
from time import sleep


###############INPUT PART###############

api_id = '22718448'
api_hash = 'aacff9e7028153dce900d87e00adfad1'
phone = '+6281374050106'
group_usernames = ['@testingzz22','@testingz90']  
trigger = ["test1", "test2","test3"]
auto = ["test4", "test5","test6"]

client = TelegramClient('anon', api_id, api_hash)

###############INPUT PART###############

async def send_random_messages():
    groups = [await client.get_entity(username) for username in group_usernames]

    while True:
        for group in groups:
            message_content = random.choice(auto)
            message = await client.send_message(group, message_content)
            await asyncio.sleep(random.randint(10, 20))
            await message.delete()

async def my_event_handler(event):
    chat_id = event.chat_id

    if "new" in event.text.lower():
            await asyncio.sleep(random.randint(10,20))
            message_content = random.choice(trigger)
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

    print("STARTING META")

    # Start message sending in the background
    asyncio.create_task(send_random_messages())

    # Register the message handler
    client.add_event_handler(my_event_handler, events.NewMessage)

    # Run the client until disconnected
    await client.run_until_disconnected()

# ====== Entry Point ======
asyncio.run(main())











