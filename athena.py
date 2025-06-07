from helpers.beanstalk import *
from helpers.validservices import *
from helpers.vmcontrol import startVM
from helpers.checkpermissions import *
from helpers.serviceinfo import *

import os, json
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

no_permission_string = "You do not have permission to run this command, ask Alyssa to add you"

async def check(ctx, service, action):

    # Checks first to see if a user can execute a command
    if not (checkPermission(ctx.message.author.id, getServiceField(service, "{}_permission".format(action)))):
        await ctx.send(no_permission_string)
        return True
    
    # Checks to see if the service is valid
    if not await check_service_reply(ctx, service):
        return True
    
    return False

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

async def check_service_reply(ctx, service):
    service_boolean = valid_service_bool(service)
    if not service_boolean:
        await ctx.send("That is not a valid service")
    return service_boolean

@bot.command(pass_context=True)
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


@bot.command(pass_context=True)
async def start(ctx, service: str):

    # Checks to see if the message is valid
    if await check(ctx, service, "start"):
        return
    
    required_service = getServiceAlias(service)

    if required_service == False:
        await ctx.send("This service does not exist")
        return
    
    match service:
        case _:
            startVM(getServiceField(required_service, "vm"))
            sendMessage("start {}".format(required_service))
            await ctx.send("Starting {} server...".format(service))


@bot.command(pass_context=True)
async def stop(ctx, service: str):

    # Checks to see if the message is valid
    if await check(ctx, service, "stop"):
        return
    
    required_service = getServiceAlias(service)

    if required_service == False:
        await ctx.send("This service does not exist")
        return
    
    match service:
        case _:
            sendMessage("stop {}".format(required_service))
            await ctx.send("Stopping {} server...".format(service))

@bot.command(pass_context=True)
async def restart(ctx, service: str):
    
    # Checks to see if the message is valid
    if await check(ctx, service, "restart"):
        return
    
    required_service = getServiceAlias(service)

    if required_service == False:
        await ctx.send("This service does not exist")
        return
    
    match service:
        case _:
            startVM(getServiceField(required_service, "vm"))
            sendMessage("restart {}".format(required_service))
            await ctx.send("Restarting {} server...".format(service))

@bot.command(pass_context=True)
async def permission(ctx, action, user):
    match action:
        case "add":
            setPermission(user, type)
            await ctx.send("Added user as type {}".format(type))
        case "remove":
            setPermission(user, type)
            await ctx.send("Removed user as type {}".format(type))


bot.run(os.getenv('DISCORD_TOKEN'))