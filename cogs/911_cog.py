import discord
from discord.ext import commands
import asyncio

class Animate911Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='911')
    async def animate911(self, ctx):
        """Animates a message related to 9/11 using emojis."""
        emojis = ['✈️☁️☁️☁️🏢🏢', '✈️☁️☁️🏢🏢', '✈️☁️🏢🏢', '✈️🏢🏢', '💥💥']
        message = "`based on true story.` ~2001: 9/11: "
        
        try:
            for emoji in emojis:
                await ctx.send(message + emoji)
                await asyncio.sleep(1)  # Wait for 1 second before sending the next emoji
        except discord.Forbidden:
            await ctx.send("I do not have permission to send messages in this channel.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred while sending a message: {e}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {e}")

async def setup(bot):
   await bot.add_cog(Animate911Cog(bot))
