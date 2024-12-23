import discord
from discord.ext import commands
import os
import sys

class RestartCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='restart')
    async def restart(self, ctx):
        """Restarts the self bot console."""
        await ctx.send("Restarting the bot...")

        try:
            # Attempt to restart the bot
            os.execv(sys.executable, ['python'] + sys.argv)
        except Exception as e:
            # Handle any exceptions that occur during the restart
            await ctx.send(f"An error occurred while trying to restart: {e}")

async def setup(bot):
   await bot.add_cog(RestartCog(bot))
