import discord
from scraper import find_mmr
from secret import TOKEN_DISCORD

client = discord.Client()

@client.event

async def on_ready():
    print(f'We have logged in as {client}')

@client.event

async def on_message(message):
    if (message.author == client.user):
        return 
    if (message.content.startswith('$mmr')):
        await message.channel.send(find_mmr(message.content.split(' ', 1)[1]))

client.run(TOKEN_DISCORD)