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

@BOT.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    react = f"Reaction {reaction.emoji} from {user.display_name}"
    channel = BOT.get_channel(1419012596899643543)
    await channel.send(react)

BOT.run(TOKEN)
