import discord
from discord.ext import commands

class DelBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_msg')
    async def delete_last_message(self, ctx):
        try:
            # Fetch the last message sent by the bot in the channel
            async for message in ctx.channel.history(limit=10):
                if message.author == self.bot.user:
                    await message.delete()
                    await ctx.send("Your last message has been deleted.", delete_after=5)
                    return
            await ctx.send("No messages found to delete.", delete_after=5)
        except discord.Forbidden:
            await ctx.send("I do not have permission to delete messages.", delete_after=5)
        except discord.HTTPException as e:
            await ctx.send(f"Failed to delete the message due to an error: {e}", delete_after=5)
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {e}", delete_after=5)

    @commands.command(name='delete_all')
    async def delete_all_messages(self, ctx):
        try:
            deleted = 0
            async for message in ctx.channel.history(limit=100):
                if message.author == self.bot.user:
                    await message.delete()
                    deleted += 1
            await ctx.send(f"Deleted {deleted} messages.", delete_after=5)
        except discord.Forbidden:
            await ctx.send("I do not have permission to delete messages.", delete_after=5)
        except discord.HTTPException as e:
            await ctx.send(f"Failed to delete messages due to an error: {e}", delete_after=5)
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {e}", delete_after=5)

# Setup function to add the cog to the bot
async def setup(bot):
   await bot.add_cog(DelBot(bot))
