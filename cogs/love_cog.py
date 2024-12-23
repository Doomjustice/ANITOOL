from typing import List, Optional
import logging

import discord
from discord.ext import commands

from colorama import Fore
import asyncio

def get_sentences() -> List[str]:
    """Read sentences from a file and return them as a list of strings."""
    try:
        with open("assets/i_love_u.txt", "r") as file:
            sentences = file.readlines()
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
            return sentences
    except FileNotFoundError:
        print(f"[{Fore.RED}-{Fore.RESET}] Error: File 'i_love_u.txt' not found.")
        return []
    except Exception as e:
        print(f"[{Fore.RED}-{Fore.RESET}] Error: {e}")
        return []

class LoveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stop_pack_flag: bool = False
        self.delay: float = 0.5
        self.packed_messages: List[discord.Message] = []

    @commands.command()
    async def love(self, ctx, *, users: Optional[discord.User] = None) -> None:
        """Love someone."""
        await ctx.message.delete()
        self.packed_messages = []
        sentences = get_sentences()

        for sentence in sentences:
            if sentence in ["\n", "", " "]:
                sentences.remove(sentence)
            if self.stop_pack_flag:
                self.stop_pack_flag = False
                return

            try:
                if users:
                    message = await ctx.send(f"# {users.mention} {sentence.strip()}")
                else:
                    message = await ctx.send(f"# {sentence.strip()}")
                self.bot.logger.info(f"Message Sent: ♰ {sentence.strip()}")
                self.packed_messages.append(message)
            except Exception as e:
                self.bot.logger.error(f"An error occurred: {e}")
            await asyncio.sleep(self.delay)

    @commands.command()
    async def stop_love(self, ctx) -> None:
        """Stop stops the love spam."""
        try:
            await ctx.message.delete()
            self.stop_pack_flag = True

            self.bot.logger.debug("Stopped spamming ILY")
            temp_message = await ctx.send("`Stopped loving`")
            await asyncio.sleep(3)
            await temp_message.delete()
        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command()
    async def speed(self, ctx, new_delay: float) -> None:
        """Set the delay between each message in the pack."""
        try:
            await ctx.message.delete()
            self.delay = new_delay

            self.bot.logger.debug(f"Delay set to: {new_delay}")
            temp_message = await ctx.send(f"Delay set to `{new_delay}`")
            await asyncio.sleep(3)
            await temp_message.delete()
        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command()
    async def delete_love(self, ctx) -> None:
        """Delete love"""
        await ctx.message.delete()
        for message in self.packed_messages:
            try:
                await message.delete()
                self.bot.logger.info(f"Message Deleted: {message.content}")
            except discord.errors.NotFound:
                self.bot.logger.error(f"Message not found: {message.content}")
            except Exception as e:
                self.bot.logger.error(f"An error occurred: {e}")

        self.packed_messages = []

async def setup(bot):
    await bot.add_cog(LoveCog(bot))