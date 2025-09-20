import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands import register_commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.members = True

BOT = commands.Bot(command_prefix='/', intents=intents)
TREE = BOT.tree

@BOT.event
async def on_ready() -> None:
    print(f"Logged in as {BOT.user}")
    await BOT.change_presence(activity=discord.Game('Yay CS!!'))

    await register_commands(BOT, TREE)

BOT.run(TOKEN)