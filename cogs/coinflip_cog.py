from typing import Dict, Set, Optional
import random
import asyncio
from discord.ext import commands

class CoinFlipCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        # Delete the command trigger message
        await ctx.message.delete()

        # Initial message
        message = await ctx.send("Flipping the coin...")

        # Animation loop
        for _ in range(5):  # Adjust the range for longer/shorter animation
            # Alternate between "Heads 🪙" and "Tails 🪙"
            if _ % 2 == 0:
                await message.edit(content="Heads 🪙")
            else:
                await message.edit(content="Tails 🪙")
            await asyncio.sleep(0.4)  # Adjust the sleep time for speed of animation

        # Final result
        result = self.coin_flip()
        await message.edit(content=result)

    def coin_flip(self):
        return "Heads 🪙" if random.randint(0, 1) == 0 else "Tails 🪙"

async def setup(bot):
    await bot.add_cog(CoinFlipCog(bot))