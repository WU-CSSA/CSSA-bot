import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
tree = bot.tree

@bot.event
async def on_ready() -> None:
    await bot.change_presence(activity=discord.Game('Yay CS!!'))
    print(f"Logged in as {bot.user}")

# ping, tests latency
@tree.command(name="ping", description="Tests the bot's latency.")
async def ping(inter: discord.Interaction) -> None:
    """Get the bot's latency"""
    await inter.response.send_message(f"Pong! ({round(bot.latency * 1000)}ms)")

@bot.command()
async def sync(ctx: commands.Context) -> None:
    """Sync commands"""
    synced = await ctx.bot.tree.sync()
    await ctx.send(f"Synced {len(synced)} commands globally")


bot.run(TOKEN)