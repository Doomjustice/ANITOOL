import discord
from discord.ext import commands
import asyncio

class SelfBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mimic(self, ctx):
        try:
            # Read messages from custom.txt
            with open('sentences.txt', 'r') as file:
                messages = file.readlines()

            # Check if there are enough messages
            if len(messages) < 10:
                await ctx.send("Not enough messages in custom.txt. Please add at least 10 messages.")
                return

            # Send the first 10 messages with a delay of 0 seconds
            for i in range(1):
                await ctx.send(messages[1].strip())
                await asyncio.sleep(0)  # Delay of 0 seconds

        except FileNotFoundError:
            await ctx.send("Error: custom.txt file not found. Please ensure it exists in the same directory.")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")

# Setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(SelfBot(bot))
