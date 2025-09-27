
import discord

async def register_commands(bot, tree) -> None:
    @tree.command(description="Prints the message cache")
    async def cache(inter: discord.Interaction) -> None:
        cache = [*bot.cached_messages]
        await inter.response.send_message(f"{cache}")

    @tree.command(name="ping", description="Tests the bot's latency.")
    async def ping(inter: discord.Interaction) -> None:
        """Get the bot's latency"""
        await inter.response.send_message(f"Pong! ({round(bot.latency * 1000)}ms)")

    await tree.sync()