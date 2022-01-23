from operator import truediv
import os
import discord
import requests
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

def deleteChannelTag(text):
    if "#" in text:
        return text.replace("#", "")
    return text

def translation(text):
    text = deleteChannelTag(text)
    auth_key = os.getenv('KEY')
    apiDeepl = requests.get("https://api-free.deepl.com/v2/translate?auth_key=" + auth_key + "&text=" + text +"&target_lang=FR")
    json = apiDeepl.json()
    return json['translations'][0]['text']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # News automatique
    if (message.channel.id == 722163183409954848 or message.channel.id == 849887600327262208 or 
    message.channel.id == 746738363427717193 or message.channel.id == 857318362652082199 or message.channel.id == 934836304955457536):
        news = translation(message.content)
        await message.delete()
        await message.channel.send("🎶🌮  " + news + "  🌮🎶")

        if (message.attachments):
            for img in message.attachments:
                await message.channel.send(img)


client.run(os.getenv('TOKEN'))