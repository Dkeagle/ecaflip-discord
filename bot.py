import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Importing bot modules
from modules.config import PREFIX, NAME

# Load bot token from environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the bot client
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), help_command=None)

# Event handlers
@bot.event
async def on_ready():
    print(f"{NAME} logged in!")

@bot.event
async def on_disconnect():
    print(f"{NAME} logged out!")

@bot.event
async def on_command(ctx):
    if ctx.message.author == bot.user:
        return
    splitted = ctx.message.content.split()
    if len(splitted) >= 2:
        print(f"{splitted[0]} {splitted[1:]}")
    else:
        print(f"{splitted[0]}")

@bot.event
async def on_command_error(ctx, error):
    splitted = ctx.message.content.split()
    text = f"{error}"
    if isinstance(error, commands.CommandNotFound):
        text = f"{splitted[0]}: Unknown command"
    elif isinstance(error, commands.MissingPermissions):
        text = f"{splitted[0]}: {ctx.message.author} is not allowed to execute this command"
    await ctx.send(text)
    print(text)

# Commands
@bot.command()
@commands.has_permissions(administrator=True)
async def logout(ctx):
    await bot.close()

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx):
    bot.reload_extension("modules.extensions")

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx):
    splitted = ctx.message.content.split()
    if len(splitted) == 1:
        return
    else:
        for extension in splitted[1:]:
            ext = f"modules.{extension}"
            try:
                bot.unload_extension(ext)
            except Exception as err:
                print(f"{ext} not unloaded! ({err})")
            else:
                print(f"{ext} unloaded!")

# Load the extensions handler module
bot.load_extension("modules.extensions")

# Start the bot
if __name__ == "__main__":
    bot.run(TOKEN)