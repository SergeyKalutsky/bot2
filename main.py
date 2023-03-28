from random import randint
from api_token import TOKEN
import discord
import requests

def get_duck_url():
    res = requests.get('https://random-d.uk/api/random').json()
    return res['url']


def get_fox():
    res = requests.get('https://randomfox.ca/floof/').json()
    return res['link']

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!duck':
        url = get_duck_url()
        await message.channel.send(url)
    if message.content == '!fox':
        url = get_fox()
        await message.channel.send(url)
    if message.content == 'как дела?':
        await message.channel.send('Хорошо как у тебя?')
    if message.content == 'с новым годом!':
        await message.channel.send('И тебя с праздником')
    if message.content == 'random':
        await message.channel.send(str(randint(1, 100)))
client.run(TOKEN)