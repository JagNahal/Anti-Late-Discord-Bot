import os
import discord
from conditions import CONDITIONS

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    uppercase_input = message.content.upper()

    for condition in CONDITIONS:
        for trigger in condition['triggers']:
            if trigger in uppercase_input:
                await message.channel.send(condition['gif'])


client.run(os.environ['DISCORD_TOKEN'])