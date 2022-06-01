import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Importing bot modules
from modules.config import PREFIX, NAME

# Load bot token from environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the bot client
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX))

# Event handlers
@bot.event
async def on_ready():
    print(f"{NAME} logged in!")

@bot.event
async def on_disconnect():
    print(f"{NAME} logged out!")

# Start the bot
if __name__ == "__main__":
    bot.run(TOKEN)