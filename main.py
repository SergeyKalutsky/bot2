from api_token import TOKEN
import discord
from resources import get_data, gen_resources

client = discord.Client(intents=discord.Intents.all())

# 1000 серебрянных
# Информация обновляется раз в сутки
# руда, кожа, специи, металлы, пшеница -> случайным образом определяем кол-во и цену
# Города: Линхейм, куртавия, трайтгельм, алгоритмтоун
# Переезд в другой город стоит денег и времени
# !towns
# !info Линхейм
# !buy resource


money = 1000

@client.event
async def on_message(message):
    global money
    if message.author == client.user:
        return
    if message.content == '!help':
        commands = '''Команды:
**!towns** - показывает ближайшие города
**!info город** - показывает информацию по ресурсам в городе'''
        await message.channel.send(commands)
    if message.content == '!towns':
        data = get_data()
        towns = ''
        for town_dict in data:
            towns += town_dict['town'] + '\n'
        await message.channel.send(towns)
    if '!money' in message.content:
        await message.channel.send(money)
    if '!info' in message.content:
        town = message.content.split(' ')[1]
        data = get_data()
        found = False
        for city_dict in data:
            if city_dict['town'] == town:
                found = True
                break
        if not found:
            await message.channel.send('Такого города не существует!')
            return
        resource_string = ''
        for resource in city_dict['resources']:
            resource_string += f'**{resource["name"]}**, ЦЕНА: **{resource["price"]}**, КОЛ-ВО: **{resource["amount"]}**\n\n'
        await message.channel.send(resource_string)
    if '!buy' in message.content:
        data = get_data()
        resource_user = message.content.split(' ')[1]
        amount = int(message.content.split(' ')[2])
        for city_dict in data:
            if city_dict['is_here']:
                break
        for resource in city_dict['resources']:
            if resource_user == resource['name']:
                total = resource['price'] * amount
                money -= total
                await message.channel.send('Покупка совершена')
                break


        
client.run(TOKEN)
