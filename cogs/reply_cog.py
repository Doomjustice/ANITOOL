import discord
from discord.ext import commands
import asyncio

class Reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_custom_messages()

    def load_custom_messages(self):
        """Load custom messages from a text file."""
        try:
            with open('reply.txt', 'r') as file:
                self.messages = file.readlines()
                self.messages = [msg.strip() for msg in self.messages if msg.strip()]
        except FileNotFoundError:
            print("Error: 'custom.txt' file not found.")
            self.messages = []
        except Exception as e:
            print(f"An error occurred while loading messages: {e}")
            self.messages = []

    @commands.command()
    async def auto_presser(self, ctx, user: discord.User):
        """Reply to a user five times quickly with custom messages."""
        if not self.messages:
            await ctx.send("No custom messages available to send.")
            return

        try:
            for i in range(5):
                message = self.messages[i % len(self.messages)]  # Cycle through messages
                await ctx.send(f"{user.mention} {message}")
                await asyncio.sleep(0)  # Wait for 1 second between replies
        except Exception as e:
            await ctx.send(f"An error occurred while sending messages: {e}")

# Setup function to add the cog to the bot
async def setup(bot):
   await bot.add_cog(Reply(bot))
