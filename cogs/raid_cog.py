import discord
from discord.ext import commands
import asyncio
import os

class RaidCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nigger')
    async def spam(self, ctx):
        """Sends a message from raid.txt to all channels in the server 10 times."""
        try:
            # Check if the raid.txt file exists
            if not os.path.isfile('raid.txt'):
                await ctx.send("Error: custom.txt file not found.")
                return
            
            # Read the message from custom.txt
            with open('raid.txt', 'r') as file:
                message = file.read().strip()
            
            # Check if the message is empty
            if not message:
                await ctx.send("Error: The message in custom.txt is empty.")
                return
            
            # Send the message to all channels
            for channel in ctx.guild.text_channels:
                try:
                    for _ in range(10):  # Send the message 10 times
                        await channel.send(message)
                        await asyncio.sleep(0.1)  # Short delay to avoid rate limits
                except discord.Forbidden:
                    print(f"Cannot send messages to {channel.name}. Permission denied.")
                except discord.HTTPException as e:
                    print(f"Failed to send message to {channel.name}: {e}")
        
            await ctx.send("Spam completed successfully.")
        
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

# Setup function to add the cog to the bot
async def setup(bot):
   await bot.add_cog(RaidCog(bot))
