from typing import List

from discord.ext import commands
import discord

import asyncio

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def user_info(self, ctx, user: discord.User) -> None:
        """Displays information about the mentioned user."""
        self.bot.logger.info(f"User info requested by {ctx.author.name} for {user.name}")
        try:
            await ctx.message.delete()
        except Exception as e:
            self.bot.logger.error(f"Failed to delete message: {e}")

        try:
            
            text = f"""
```
[User Info - {user.name}]

GlobalName: {user.name}
ID: {user.id}
Created At: {user.created_at}
Avatar: {user.avatar.url if user.avatar else "No Avatar"}
Bannner: {user.banner.url if user.banner else "No Banner"}

ANITOOL By DJ.
```
"""
            if user.avatar:
                text += f"[Avatar URL]({user.avatar.url})\n"
            if user.banner:
                text += f"[Banner URL]({user.banner.url})\n"

            await ctx.send(text)
        except Exception as e:
            self.bot.logger.error(f"An error occurred when sending user info: {e}")
    
    @commands.command()
    async def server_info(self, ctx) -> None:
        """Displays information about the server."""
        self.bot.logger.info(f"Server info requested by {ctx.author.name}")
        try:
            await ctx.message.delete()
        except Exception as e:
            self.bot.logger.error(f"Failed to delete message: {e}")

        if ctx.guild is None:
            temp = await ctx.send("`This command can only be used in a server.`")
            await asyncio.sleep(1.5)
            await temp.delete()
            self.bot.logger.error("This command can only be used in a server.")
            return

        try:
            guild = ctx.guild
            text = f"""
```
[Server Info - {guild.name}]

ServerName: {guild.name}
ID: {guild.id}
Created At: {guild.created_at}
Owner: {guild.owner}
Members: {guild.member_count}
Roles: {len(guild.roles)}
Channels: {len(guild.channels)}
Categories: {len(guild.categories)}
ServerIcon: {guild.icon.url if guild.icon else "No Icon"}
ServerBanner: {guild.banner.url if guild.banner else "No Banner"}

ANITOOL By DJ.
```
"""
            if guild.icon:
                text += f"[Server Icon URL]({guild.icon.url})\n"
            if guild.banner:
                text += f"[Server Banner URL]({guild.banner.url})\n"

            await ctx.send(text)

        except Exception as e:
            self.bot.logger.error(f"An error occurred when sending server info: {e}")
    
    @commands.command()
    async def gc_info(self, ctx) -> None:
        """Displays information about the global context."""
        self.bot.logger.info(f"Group Chat info requested by {ctx.author.name}")
        try:
            await ctx.message.delete()
        except Exception as e:
            self.bot.logger.error(f"Failed to delete message: {e}")

        if not isinstance(ctx.channel, discord.GroupChannel):
            self.bot.logger.error("This command can only be used in a group chat.")
            temp = await ctx.send("`This command can only be used in a group chat.`")
            await asyncio.sleep(1.5)
            await temp.delete()
            return

        group_chat: discord.GroupChannel = ctx.channel
        try:
            text = f"""
```
[Group Chat Info - {group_chat.name}]

GroupName: {group_chat.name}
ID: {group_chat.id}
Created At: {group_chat.created_at}
Owner: {group_chat.owner}
Members: {len(group_chat.recipients) + 1}
Icon: {group_chat.icon.url if group_chat.icon else "No Icon"}

ANITOOL By DJ.
```
"""
            if group_chat.icon:
                text += f"[Icon URL]({group_chat.icon.url})\n"
            await ctx.send(text)

        except Exception as e:
            self.bot.logger.error(f"An error occurred when sending group chat info: {e}")

    
    @commands.command()
    async def my_info(self, ctx) -> None:
        """Displays information about the author."""
        self.bot.logger.info(f"User info requested by {ctx.author.name}")
        try:
            await ctx.message.delete()
        except Exception as e:
            self.bot.logger.error(f"Failed to delete message: {e}")

        try:
            user = ctx.author
            text = f"""
```
[User Info - {user.name}]

Sever Count: {len(self.bot.guilds)}
Owned Servers: {len([guild for guild in self.bot.guilds if guild.owner == user])}
Friend Count: {len(self.bot.friends)}
Open DMs: {len(self.bot.private_channels)}
Blocked Users: {len(self.bot.blocked)}
Groups: {len([channel for channel in self.bot.private_channels if isinstance(channel, discord.GroupChannel)])}

ANITOOL By DJ.
```
"""
            await ctx.send(text)
        except Exception as e:
            self.bot.logger.error(f"An error occurred when sending user info: {e}")

    @commands.command()
    async def services(self, ctx) -> None:
        """Displays information about the services."""
        self.bot.logger.info(f"Services info requested by {ctx.author.name}")
        try:
            await ctx.message.delete()
        except Exception as e:
            self.bot.logger.error(f"Failed to delete message: {e}")

        try:
            response_cog = self.bot.get_cog("ResponseCog")
            reactions_cog = self.bot.get_cog("ReactionsCog")
            util_cog = self.bot.get_cog("UtilCog")
            

            text = f"""
```
[Running Services]

Nitro Sniper / ON
Message Sniper / ON
Auto Responder / {"ON" if response_cog and response_cog.auto_response_message is not None else "OFF"}
Auto Reactor / {"ON" if reactions_cog and reactions_cog.auto_react_user is not None else "OFF"}
Auto Reader / {"ON" if util_cog and util_cog.auto_read_channel is not None else "OFF"}
User Responder / {"ON" if response_cog and response_cog.response_user_message is not None else "OFF"}
Copy Cat / {"ON" if util_cog and response_cog.copy_cat_user is not None else "OFF"}

ANITOOL by DJ.
```
"""
            await ctx.send(text)
        except Exception as e:
            self.bot.logger.error(f"An error occurred when sending services info: {e}")

    @commands.command(name="bot_info")
    async def selfbot_info(self, ctx) -> None:
        """Displays information about the bot."""
        self.bot.logger.info(f"Bot info requested by {ctx.author.name}")
        try:
            await ctx.message.delete()
        except Exception as e:
            self.bot.logger.error(f"Failed to delete message: {e}")

        try:
            text = f"""
```
[ANITOOL - Info]

Download Link ~ Soon..
Creator ~ DJ.
Version ~ 2.0.0

ANITOOL by DJ.
```"""
            await ctx.send(text)
        except Exception as e:
            self.bot.logger.error(f"An error occurred when sending bot info: {e}")
            

async def setup(bot):
    await bot.add_cog(InfoCog(bot))
