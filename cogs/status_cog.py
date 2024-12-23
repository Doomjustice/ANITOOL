import discord
from discord.ext import commands, tasks
import asyncio

class StatusRotator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statuses = self.load_statuses()
        self.current_status_index = 0
        self.is_rotating = False

    def load_statuses(self):
        try:
            with open('statuses.txt', 'r') as file:
                statuses = [line.strip() for line in file if line.strip()]
            if not statuses:
                raise ValueError("The status list is empty.")
            return statuses
        except FileNotFoundError:
            print("Error: 'statuses.txt' file not found.")
            return []
        except Exception as e:
            print(f"An error occurred while loading statuses: {e}")
            return []

    @commands.command(name='status')
    async def start_rotating(self, ctx):
        if not self.is_rotating:
            self.is_rotating = True
            self.rotate_status.start()
            await ctx.send("`Status rotation started.`")

    @commands.command(name='stop_status')
    async def stop_rotating(self, ctx):
        if self.is_rotating:
            self.is_rotating = False
            self.rotate_status.stop()
            await ctx.send("`Status rotation stopped.`")

    @tasks.loop(seconds=3)
    async def rotate_status(self):
        if self.is_rotating and self.statuses:
            status = self.statuses[self.current_status_index]
            activity = discord.Streaming(name=status, url="https://twitch.tv/jxtice")  # Replace with your channel
            await self.bot.change_presence(activity=activity)
            self.current_status_index = (self.current_status_index + 1) % len(self.statuses)

    @rotate_status.before_loop
    async def before_rotate_status(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(StatusRotator(bot))
