import discord
from discord.ext import commands
import asyncio

class AfkCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_counting = False
        self.counter_task = None

    @commands.command(name='afk')
    async def start_count(self, ctx, user: discord.User):
        """Starts counting from 1 to 100 and mentions the user."""
        if self.is_counting:
            await ctx.send("afk checker already running lil bro")
            return
        
        self.is_counting = True
        await ctx.send(f"AFK CHECK BITCH! {user.mention}, LOL")

        try:
            self.counter_task = self.bot.loop.create_task(self.count_to_100(ctx))
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
            self.is_counting = False

    async def count_to_100(self, ctx):
        """Counts from 1 to 100."""
        for i in range(1, 101):
            await ctx.send(i)
            await asyncio.sleep(0.0)  # Adjust the speed of counting
        self.is_counting = False

    @commands.command(name='afk_stop')
    async def stop_count(self, ctx):
        """Stops the counting process."""
        if not self.is_counting:
            await ctx.send("No afk checker is in progress.")
            return
        
        self.is_counting = False
        if self.counter_task:
            self.counter_task.cancel()
            await ctx.send("STOPPED AFK CHECKER.")

async def setup(bot):
   await bot.add_cog(AfkCog(bot))
