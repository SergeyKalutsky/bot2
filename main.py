from random import randint
from api_token import TOKEN
import discord



client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'как дела?':
        await message.channel.send('Хорошо как у тебя?')
    if message.content == 'с новым годом!':
        await message.channel.send('И тебя с праздником')
    if message.content == 'random':
        await message.channel.send(str(randint(1, 100)))
client.run(TOKEN)