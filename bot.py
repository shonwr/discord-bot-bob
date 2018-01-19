import discord
from discord.ext.commands import Bot
from urllib.parse import urlencode
import secrets
import asyncio
import time
import sys


bob_the_builder = Bot(command_prefix="!")

@bob_the_builder.event
async def on_read():
    print('Client logged in')

@bob_the_builder.command()
async def bob(*args):
    return await bob_the_builder.say("Who is Bob, you ask? Bob is the greatest human being ever conceived.")

@bob_the_builder.command()
async def bless(*args):
    return await bob_the_builder.say(":sparkles: You have been blessed by Bob")

@bob_the_builder.command()
async def youtube(*args):
    print(args)
    url = ("https://www.youtube.com/results?{}".format(urlencode({'search_query': ' '.join(args)})))  
    return await bob_the_builder.say("Got'em! Here are your results : \n \n %s" % url)

bob_the_builder.run(secrets.BOT_TOKEN)