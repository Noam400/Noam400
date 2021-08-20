import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return



    if message.content.startswith('בוקר טוב'):
        await message.channel.send('בוקר טוב גם לך ')
    if message.content.startswith('מה נשמע'):
        await message.channel.send('סבבה אתה יודע הילדים בסדר והאישה גם. מה איתך?')


client.run('ODc4MTM2NzE5MzM2MTU3MjE0.YR8yjA.1gLnl40sgOU8v4qCupWexRxOEqY')
