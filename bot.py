import discord
from discord.ext.commands import Bot
from urllib.parse import urlencode
import secrets
import aiohttp
import asyncio
import time
import os
import sys
import random


bob_the_builder = Bot(command_prefix="!")

@bob_the_builder.event
async def on_read():
    print('Client logged in')

#bobnr1
@bob_the_builder.command()
async def bob(*args):
    return await bob_the_builder.say("Who is Bob, you ask? Bob is the greatest human being ever conceived.")

#bless 
@bob_the_builder.command()
async def bless(*args):
    return await bob_the_builder.say(":sparkles: You have been blessed by Bob")

#youtube 
@bob_the_builder.command()
async def youtube(*args):
    print(args)
    url = ("https://www.youtube.com/results?{}".format(urlencode({'search_query': ' '.join(args)})))  
    return await bob_the_builder.say("Got'em! Here are your results : \n \n %s" % url)

#rng 
@bob_the_builder.command(pass_context=True)
async def blessrng(ctx):
    x = random.randint(1, 100)
    await bob_the_builder.send_message(ctx.message.channel, "<:BlessRNG:403833576313061387>\n \n" + "RNGesus gives you a " + "__**" + str(x) + "**__")

#random map drop 
@bob_the_builder.command()
async def drop(*args):
    drop = ['school :school:', 'roz :house:', 'pochinki(mah city):homes: ', 'prison :cop: ', 'mylta :house_abandoned:', 'primo :house_with_garden:', '*pick* :map:']
    return await bob_the_builder.say("__**" + random.choice(drop) + "**__")

#flip 
@bob_the_builder.command()
async def flip(*args):
    drop = ['Heads :monkey_face:','Tails :monkey: ']
    return await bob_the_builder.say("__**" + random.choice(drop) + "**__")
 

bob_the_builder.run(secrets.BOT_TOKEN)
