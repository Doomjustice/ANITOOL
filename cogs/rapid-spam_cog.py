import discord
from discord.ext import commands
import asyncio

class RapidSpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.messages = self.load_messages("messages.txt")

    def load_messages(self, filename):
        try:
            with open(filename, 'r') as file:
                messages = file.readlines()
                return [message.strip() for message in messages if message.strip()]
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return []
        except Exception as e:
            print(f"An error occurred while loading messages: {e}")
            return []

    @commands.command(name='rapid_spam')
    async def spam(self, ctx, delay: float = 0.0):
        if not self.messages:
            await ctx.send("No messages to send. Please check your messages.txt file.")
            return

        try:
            while True:
                for message in self.messages:
                    await ctx.send(message)
                    await asyncio.sleep(delay)
        except discord.Forbidden:
            await ctx.send("I don't have permission to send messages in this channel.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
   await bot.add_cog(RapidSpamCog(bot))
 