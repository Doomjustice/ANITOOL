from typing import Dict, Set, Optional
import discord
from discord.ext import commands

class Gc2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_flag = True  # Control flag for the spam loop

    @commands.command()
    async def g(self, ctx: str) -> None:
        """Automatically change the group channel name."""
        
        await ctx.message.delete()
        count: int = 0
        channel: discord.abc.GuildChannel = ctx.channel

        # Load names from custom.txt
        try:
            with open('custom.txt', 'r') as file:
                names = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.bot.logger.error("custom.txt file not found.")
            await ctx.send("Error: custom.txt file not found.")
            return
        except Exception as e:
            self.bot.logger.error(f"An error occurred while reading custom.txt: {e}")
            await ctx.send("Error: Unable to read custom.txt.")
            return

        while self.spam_flag:
            try:
                # Use modulo to cycle through names
                name = names[count % len(names)]
                await channel.edit(name=f"{name} x{count}")
                self.bot.logger.info(f"Changed channel name to: {name} x{count}")
                count += 1
            except discord.Forbidden:
                self.bot.logger.error("Permission denied to change channel name.")
                await ctx.send("Error: Permission denied to change channel name.")
                break
            except Exception as e:
                self.bot.logger.error(f"An error occurred: {e}")
                await ctx.send(f"Error: {e}")
                break

    
    @commands.command()
    async def stop(self, ctx: str) -> None:
        """Stop the channel name spamming."""
        self.spam_flag = False
        await ctx.send("`Stopped. use >bypass to disable limit.`")
        await asyncio.sleep(3)
        await temp_message.delete()


    @commands.command()
    async def bypass(self, ctx) -> None:
        """Stops limit"""
        try:
            await ctx.message.delete()
            self.spam_flag = True
            self.bot.logger.debug("Bypassed The Limit")
            await ctx.send("`Bypassed Rate Limit`")
            await asyncio.sleep(3)
            await temp_message.delete()
        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")
            


async def setup(bot):
    await bot.add_cog(Gc2(bot))