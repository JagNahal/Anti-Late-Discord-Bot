# https://github.com/Rapptz/discord.py
import discord
import os
import time
from discord.ext import commands
from nltk.sentiment import SentimentIntensityAnalyzer

client = discord.Client()
sia = SentimentIntensityAnalyzer()

async def punish_sad_people(msg):
    sentiment = sia.polarity_scores(msg.content)
    print(sentiment)
    
    if sentiment['compound'] < 0:
        await msg.channel.send('https://c.tenor.com/IweIMqGS1gkAAAAC/questioning-are-you-sad.gif')
    

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    late_strings = ["I AM LATE", "IM LATE", "I'M LATE"]
    if message.author == client.user:
        return
    uppercase_input = message.content.upper()
    await punish_sad_people(message)

    for late_string in late_strings:
        if late_string in uppercase_input:
            await message.channel.send('https://tenor.com/baxTB.gif')



# bot = commands.Bot(command_prefix='>')

# @bot.command()
# async def here(ctx):
#     await ctx.send(time.time())

# bot.run(os.environ['DISCORD_TOKEN'])
client.run(os.environ['DISCORD_TOKEN'])
