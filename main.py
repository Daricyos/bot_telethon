from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
import random, os
import glob
import config


api_id = config.IDapi
api_hash = config.HashApi

client = TelegramClient('anon', api_id, api_hash)

list_name = []

async def main():
    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
    dir = os.path.abspath(os.path.join('photo'))
    all_pngs =  glob.glob("./photo/*.jpg") + glob.glob("./photo/*.jpeg")
    random_filename = random.choice(all_pngs)
    await client(UploadProfilePhotoRequest(await client.upload_file(random_filename)))

    with open("name.txt") as rnd:
        for line in rnd:
            line=line.strip()
            list_name.append(line)

    one_name = list_name[random.randint(0,len(list_name)-1)]

    await client(UpdateProfileRequest(first_name=one_name))


with client:
    client.loop.run_until_complete(main())