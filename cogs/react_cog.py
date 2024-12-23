from typing import Optional, Union
import logging

import discord
from discord.ext import commands

import asyncio


class AutoReactCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_react_user: Optional[Union[discord.User, str]] = None
        self.auto_react_emojis: Optional[str] = None
        self.auto_react_channel: Optional[discord.TextChannel] = None

    async def convert_to_emoji(self, emoji_str: str) -> Union[discord.Emoji, str]:
        """Converts a string to a discord.Emoji object if it's a custom emoji, else returns the string."""

        if emoji_str.startswith("<:") and emoji_str.endswith(">"):
            emoji_id = int(emoji_str.split(":")[-1][:-1])
            emoji = self.bot.get_emoji(emoji_id)
            return emoji or emoji_str
        return emoji_str

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """Listens for messages and reacts with the auto react emojis if set."""

        if self.auto_react_emojis and self.auto_react_user:
            if (
                self.auto_react_user == "@everyone"
                or message.author == self.auto_react_user
            ):
                if self.auto_react_channel:
                    if message.channel != self.auto_react_channel:
                        return
                    
                for emoji in self.auto_react_emojis.split():
                    try:
                        await message.add_reaction(await self.convert_to_emoji(emoji))
                        self.bot.logger.info(f"Auto reacted with: {emoji}")
                    except discord.HTTPException:
                        self.bot.logger.error(f"Failed to add emoji: {emoji}")
                    except Exception as e:
                        self.bot.logger.error(f"An error occurred: {e}")

    @commands.command()
    async def react2(self, ctx, users: str, *, emojis: str) -> None:
        """Automatically react to messages from the provided users with the specified emojis."""
        
        # Split the users string into a list
        user_list = [user.strip() for user in users.split(',')]
        
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            self.bot.logger.error("Message not found.")
        except Exception as e:
            self.bot.logger.error(f"An error occurred while deleting the message: {e}")

        for user in user_list:
            if user != "@everyone":
                try:
                    user_obj = await commands.UserConverter().convert(ctx, user)
                    self.auto_react_user = user_obj
                except commands.UserNotFound:
                    temp_message = await ctx.send(f"User `{user}` not found.")
                    await asyncio.sleep(3)
                    await temp_message.delete()
                    continue  # Skip to the next user
            else:
                self.auto_react_user = "@everyone"
                self.auto_react_channel = ctx.channel

            self.auto_react_emojis = emojis
            self.bot.logger.debug(f"Auto reacting with emojis: {emojis} for user: {user}")
            temp_message = await ctx.send(
                f"Reacting with {emojis} for user: {user}"
            )
            await asyncio.sleep(3)
            await temp_message.delete()

# Setup function to add the cog to the bot
async def setup(bot):
   await bot.add_cog(AutoReactCog(bot))
