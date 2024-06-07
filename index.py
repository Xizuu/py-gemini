import aiohttp
import asyncio

async def send_request():
    url = 'https://react-gemini-api.vercel.app/gemini'
    token = 'your token' # https://aistudio.google.com/app/apikey
    
    while True:
        ask = input("Masukkan pesan atau ketik 'exit' untuk keluar: ")
        if ask.lower() == 'exit':
            print("Terima kasih telah menggunakan program ini :)")
            break
        
        data = {
            "token": token,
            "content": {
                "user": "user",
                "message": ask
            }
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as r:
                result = await r.json()
                print("Respon:", result['response'])

asyncio.run(send_request())

