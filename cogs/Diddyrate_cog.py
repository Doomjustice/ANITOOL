import random
import asyncio
from discord.ext import commands

class DiddyRateCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='diddyrate')
    async def diddyrate(self, ctx, member: commands.MemberConverter):
        # Initial message
        message = await ctx.send(f"Calculating diddy rate for {member.mention}...")

        # Animation loop
        for _ in range(5):  # Adjust the range for longer/shorter animation
            await message.edit(content=f"Calculating diddy rate for {member.mention}... {random.randint(0, 100)}%")
            await asyncio.sleep(0.5)  # Adjust the sleep time for speed of animation

        # Final result with modification for @konuri_en
        if member.name == "konuri_en":  # Check if the member is @konuri_en
            final_rate = random.randint(50, 100)  # Ensure rate is 50 or higher
        else:
            final_rate = random.randint(0, 100)  # Normal rate for others

        await message.edit(content=f"{member.mention}'s diddy rate is: **{final_rate}%**")

async def setup(bot):
    await bot.add_cog(DiddyRateCog(bot))