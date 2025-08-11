from telethon import TelegramClient, events
import asyncio
import random
from random import randint
from time import sleep


###############INPUT PART###############

api_id = '22718448'
api_hash = 'aacff9e7028153dce900d87e00adfad1'
phone = '+6281374050106'
group_ids = ["@testingzz22","@testingz90"]  
trigger = ["test1","test2","test3"]

automsg = ["Menurut gue, ini langkah yang mantap buat nge-refresh lini depan MU, apalagi dengan gaya mainnya yang fisikal dan cepat.",
"Lo pikir dia langsung bisa nyatu sama sistem Reuben Amorim, atau masih perlu adaptasi?",
"iya gue baca juga. Secara gaya main, sih, Sesko punya atribut super keren tnggi, kuat, lari cepat, plus punya kemampuan aerial yang mumpuni.",
"Dia sempat jadi top scorer di Leipzig, dan ada catatan dia bikin total 39 gol dari 87 penampilan sejak datang dari Salzburg",
"tapi, gue juga mikir transfer mahal itu juga bawa beban tinggi ke pundaknya.",
"Harga segitu, fans pasti expect dia langsung ngegemparin EPL. Luka adaptasi liga Inggris kan bisa bikin pressure makin berat. Dan MU sendiri lagi banyak belanja striker Cunha, Mbeumo, dan sekarang Sesko. Apakah ini jadi duplikat di lini depan? Atau mereka membangun rotasi yang tajam?",
"Guys, gue cuma mau sorotin satu hal finansialnya. Dari laporan, United sekarang lagi di tengah-musim spending galore, bro over £200m buat three new forwards dan totalnya bisa tembus £245m+",
"yaa sementara itu, dia juga lagi harus manage kerugian ratusan juta, perencanaan stadion £2miliar, dan PSR Profit‑sustainability rules",
"Gila. Jadi, investasi ke Sesko bukan cuma soal performa, tapi juga gimana caranya bayar tanpa bikin klub collapse.",
"ges, pemilihan Sesko ini lebih karena potensinya sebagai striker masa depan, atau karena strategi merchandising & hype belaka?",
"lu sih selalu bawa-bawa finansial mulu, bikin pusing pala barbie. Tapi gue ngerti sih poin lo, apalagi MU sekarang udah nggak bisa seenaknya belanja tanpa mikir efeknya ke aturan keuangan klub.",
"Tapi ya, dari sisi fans, kita udah lama nggak punya striker muda yang bener-bener bikin jantungan tiap kali dapet bola di kotak penalti. Sesko tuh potensial banget buat jadi bintang baru, mirip Haaland dari segi fisik dan pergerakan.",
"Gila men, dia tinggi, larinya cepet, finishingnya dingin. Kalo dikasih waktu dan sistem yang pas, dia bisa jadi striker utama bertahun-tahun ke depan. Bukan cuma buat United, tapi buat Liga Inggris juga.",
"Lu bayangin aja kombinasi dia sama Garnacho di sisi kiri, Bruno ngumpan di belakang, itu mah horror buat tim lawan.",
"Gue ngelihat Sesko itu sebagai investasi jangka panjang. Tapi tetep, gue masih khawatir dia bakal keteken ekspektasi terlalu dini.",
"Fans MU itu kan terkenal nggak sabaran, dikit-dikit dibandingin sama legenda kayak Van Persie, Rooney, bahkan Ronaldo."]

client = TelegramClient('anon', api_id, api_hash)

###############INPUT PART###############

async def send_random_messages():

      while True:
        for group_id in group_ids:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_id, message_auto)        
            await asyncio.sleep(random.randint(10,20))

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

















