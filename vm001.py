from helpers.beanstalk import *

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

description = '''Athenaserver Discord Bot'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)

load_dotenv()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def start(ctx, service: str):
    match service:
        case _:
            sendMessage("start {}".format(service))
            await ctx.send("Starting {} server...".format(service))

@bot.command()
async def stop(ctx, service: str):
    match service:
        case _:
            sendMessage("stop {}".format(service))
            await ctx.send("Stopping {} server...".format(service))

@bot.command()
async def restart(ctx, service: str):
    match service:
        case _:
            sendMessage("restart {}".format(service))
            await ctx.send("Restarting {} server...".format(service))

print(os.getenv('DISCORD_TOKEN'))

bot.run(os.getenv('DISCORD_TOKEN'))