import random
import asyncio
from discord.ext import commands

class GayRateCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='gayrate')
    async def gayrate(self, ctx, member: commands.MemberConverter):
        # Initial message
        message = await ctx.send(f"Calculating gay rate for {member.mention}...")

        # Animation loop
        for _ in range(5):  # Adjust the range for longer/shorter animation
            await message.edit(content=f"Calculating gay rate for {member.mention}... {random.randint(0, 100)}%")
            await asyncio.sleep(0.5)  # Adjust the sleep time for speed of animation

        # Final result
        final_rate = random.randint(0, 100)
        await message.edit(content=f"{member.mention}'s gay rate is: **{final_rate}%** 🌈")

async def setup(bot):
    await bot.add_cog(GayRateCog(bot))