from random import randint
from api_token import TOKEN
import discord
import requests
import wikipedia
from api import vicorina
from chat_gpt_api import talk_to_chatGPT_who_are_cheap

wikipedia.set_lang("ru")


def search_wiki(search):
    lst = wikipedia.search(search)
    if lst:
        res = wikipedia.page(lst[0])
        return res.title, res.url


def get_duck_url():
    res = requests.get('https://random-d.uk/api/random').json()
    return res['url']


def get_fox():
    res = requests.get('https://randomfox.ca/floof/').json()
    return res['link']


client = discord.Client(intents=discord.Intents.all())


state = ''
answer = ''
help_ans = ''


@client.event
async def on_message(message):
    global state, answer, help_ans
    if message.author == client.user:
        return
    await message.channel.send('Генерирую ответ...')
    chat_response = talk_to_chatGPT_who_are_cheap(message.content)
    await message.channel.send(chat_response)
    # if state == 'game':
    #     if message.content == answer:
    #         await message.channel.send('Правильно')
    #         question, answer = vicorina()
    #         help_ans = ''
    #         await message.channel.send(question)
    #     else:
    #         help_ans = answer[:len(help_ans) + 1]
    #         await message.channel.send(f'{help_ans}')
    #     return 
    # if message.content == '!game':
    #     question, answer = vicorina()
    #     state = 'game'
    #     await message.channel.send(question)
    #     return
    # if 'wiki' in message.content:
    #     search = ' '.join(message.content.split(' ')[1:])
    #     res = search_wiki(search)
    #     if res:
    #         await message.channel.send(f'{res[0]}]\n{res[1]}')
    # if message.content == '!duck':
    #     url = get_duck_url()
    #     await message.channel.send(url)
    # if message.content == '!fox':
    #     url = get_fox()
    #     await message.channel.send(url)
    # if message.content == 'как дела?':
    #     await message.channel.send('Хорошо как у тебя?')
    # if message.content == 'с новым годом!':
    #     await message.channel.send('И тебя с праздником')
    # if message.content == 'random':
    #     await message.channel.send(str(randint(1, 100)))
        
client.run(TOKEN)
