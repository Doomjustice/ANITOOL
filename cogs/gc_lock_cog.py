import discord
from discord.ext import commands

class GroupChatManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_running = False

    @commands.command(name='lock.gc')
    async def start(self, ctx):
        """Start the group chat management."""
        if self.is_running:
            await ctx.send("The bot is already running.")
            return
        
        self.is_running = True
        await ctx.send("Group chat locked!")
        self.lock_group_chat(ctx)

    @commands.command(name='unlock.gc')
    async def stop(self, ctx):
        """Stop the group chat management."""
        if not self.is_running:
            await ctx.send("The bot is not running.")
            return
        
        self.is_running = False
        await ctx.send("Group chat unlocked.")

    async def lock_group_chat(self, ctx):
        """Lock the group chat and monitor users."""
        while self.is_running:
            try:
                # Lock the group chat
                await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
                await ctx.send("Group chat locked.")
                
                # Monitor for users leaving
                @self.bot.event
                async def on_member_remove(member):
                    if member in ctx.guild.members:
                        await ctx.send(f"{member.name} has left the group. Adding them back...")
                        await ctx.guild.add_member(member)
                        await ctx.send(f"{member.name} has been added back to the group.")
                
                await asyncio.sleep(1)  # Check every 10 seconds
            except discord.Forbidden:
                await ctx.send("I do not have permission to lock the group chat.")
                self.is_running = False
            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}")
                self.is_running = False

async def setup(bot):
   await bot.add_cog(GroupChatManager(bot))
