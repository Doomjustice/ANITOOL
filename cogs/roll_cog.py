from typing import Dict, Set, Optional
import random
import asyncio
from discord.ext import commands

class DiceRollCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def roll(self, ctx):
        # Initial message
        message = await ctx.send("Rolling the dice...")

        # Animation loop
        for _ in range(5):  # Adjust the range for longer/shorter animation
            await message.edit(content=str(random.randint(1, 6)))  # Show a random number between 1 and 6
            await asyncio.sleep(0.5)  # Adjust the sleep time for speed of animation

        # Final result
        result = self.roll_dice()
        await message.edit(content=f"You rolled a {result} 🎲")

    def roll_dice(self):
        return random.randint(1, 6)  # Return a random number between 1 and 6

async def setup(bot):
    await bot.add_cog(DiceRollCog(bot))