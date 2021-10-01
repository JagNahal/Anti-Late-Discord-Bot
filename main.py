# https://github.com/Rapptz/discord.py
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    late_strings = ["I AM LATE", "IM LATE", "I'M LATE"]
    if message.author == client.user:
        return
    uppercase_input = message.content.upper()

    for late_string in late_strings:
        if late_string in uppercase_input:
            await message.channel.send('https://tenor.com/baxTB.gif')
            


client.run(os.environ['DISCORD_TOKEN'])
