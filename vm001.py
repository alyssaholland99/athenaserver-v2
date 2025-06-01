from helpers.beanstalk import *
from helpers.validservices import *
from helpers.vmcontrol import startVM

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

description = '''Athenaserver Discord Bot'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents, help_command=None)

load_dotenv()

actions = ["start", "stop", "restart"]
services = ["minecraft", "ftb", "sotf", "valheim", "beam"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

async def check_service_reply(ctx, service):
    service_boolean = valid_service_bool(service)
    if not service_boolean:
        await ctx.send("That is not a valid service")
    return service_boolean

@bot.command()
async def help(ctx):
    helpText = "Syntax: `.[action] [service]`\n"

    helpText += "\nActions:\n"
    for action in actions:
        helpText += "- {}\n".format(action)

    helpText += "\nServices:\n"
    for service in services:
        helpText += "- {}\n".format(service)

    helpText += "Example `.start minecraft`"

    await ctx.send(helpText)               


@bot.command()
async def start(ctx, service: str):
    if not await check_service_reply(ctx, service):
        return
    match service:
        case _:
            startVM("vm002")
            sendMessage("start {}".format(convert_for_beanstalk(service)))
            await ctx.send("Starting {} server...".format(service))

@bot.command()
async def stop(ctx, service: str):
    if not await check_service_reply(ctx, service):
        return
    match service:
        case _:
            sendMessage("stop {}".format(convert_for_beanstalk(service)))
            await ctx.send("Stopping {} server...".format(service))

@bot.command()
async def restart(ctx, service: str):
    if not await check_service_reply(ctx, service):
        return
    match service:
        case _:
            startVM("vm002")
            sendMessage("restart {}".format(convert_for_beanstalk(service)))
            await ctx.send("Restarting {} server...".format(service))

bot.run(os.getenv('DISCORD_TOKEN'))