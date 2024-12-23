from typing import List

from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.HELPLIST: List[str] = [
"""
```
---------------------
ANITOOL BY DJ
---------------------
Prefix : >

use >search-[command]
No Space.
---------------------
packing 
auto_response
misc
gc
reactions
spam
admin
info
more
msg
services
bot_info
afk
------------------------------------------
quit / Quits The Bot
restart / Restarts the bot
------------------------------------------
ANITOOL by @DJ ♰ We Destroy Everything. ♰
------------------------------------------
If You Need help with search commands use >search-command
Do Not Use Space like >search nigga
------------------------------------------
```""",
"""
```
----------------
[Pack Commands]
-------------------------------------------------------------------
mimic / mimic a user.
k / kill a user.
lol / stops killing.
delete / deletes last msg.
set_user_response.large / auto response to a user with large space.
--------------------------------------------------------------------
ANITOOL by DJ.
--------------
```
""",
"""
```
----------------
[Auto response]
--------------------------------------------------------------------------
auto_presser / Auto presser
set_delay (delay) / Sets delay between messages
set_response [2;34m(message)[2;34m / Sets auto response on pings
disable_response / Disables auto response
copy_cat (user) / Copies everything the user says
stop_copy_cat / Stops Copy Cat
set_user_response (user) (message) / Sets auto response for a user
set_user_response.large (user) (message) / Sets auto response for large msg
stop_user_response / Stops User Response
-----------------------------------------------------------------------------

ANITOOL by DJ.
--------------
```
""",
"""
```
------------
[GC Commands]
----------------------------
call / start calling
end_call / ends current call.
stop_call / stops call
lock_gc / Locks Current GC
unlock_gc / Unlocks Locked GC
gc / Spam GC name
gc_stop / Stops GC name spam
leave_all_gcs  (Optional[exceptions by ids]) / Leaves all groups
mass_add (user/s) / Adds and removes user from a GC.
stop_mass_add / Stops Mass Adding
g / Start Renaming GC With custom text 
stop / Stops renaming gc
bypass / Bypasses The limit of g
bypass_limit / Bypasses The Limit So you can use GC Spam Again.[Automated]
---------------------------------------------------------------------------
ANITOOL by DJ.
---------------
``` 
""",
"""
```
--------------------
[Reaction Commands]
----------------------------------------------------------------
react (users) (emojis) / Auto reacts to multiple users messages 
stopreact / stops react
react (user) (emojis) / Auto Reacts to messages
stop_react / Stops auto reacting
add_reactions (bomb/emojis) / Adds Reactions
----------------------------------------------------------------
ANITOOL by DJ.
---------------
```
""",
"""
```
---------------
[Spam Commands]
-----------------------------------------------------
spam (message) / Starts Spamming the defined message.
stop_spam / Stops Spamming
delete_spam / Deletes Last Spam

ghost_ping (user) / Spam Ghost Pings user
stop_ghost_ping / Stops Ghost Pinging
-----------------------------------------------------
ANITOOL by DJ.
-----------------------------------------------------
""",
"""
```
---------------
[Info Commands]
----------------------------------
user_info (user) / Shows User Info
server_info / Shows Server Info
gc_info  / Shows Group chats Info
my_info  / Shows Your Info
-----------------------------------
ANITOOL by DJ.
--------------
```
""",
"""
```
----------------
[Admin Commands]
---------------------------------------------
nuke / Nukes A channel.
lock / Locks Current Channel
kick (user) (Optional[reason]) / Kicks A USer
ban (user) (Optional[reason]) / Bans A User
----------------------------------------------
ANITOOL by DJ.
--------------
```
""",
"""
```
---------------
[Misc Commands]
---------------------------------------------------------------------
snipe (number) / Snipes last deleted message
copy_server (ServerID_from) (serverID_to) / Copys A Server
report_message (ReplyToMessage/MessageLink) / Mass Reports a Messages
auto_read / Auto Reads Message
disable_auto_read / Stops Auto Reading
mass_dm (message) / Mass Dms all friends + open dms
ping / Shows Bot Latency
translate (text) / Translate Text to English
quit / Quits The Bot
----------------------------------------------------------------------
ANITOOL by DJ
-------------
```
""",
"""
```
---------------
[More Commands]
------------------------------------------
roll / roll a dice.
gayrate / check if user is gay.
love {user} / Spam I love you : 1% to 100%
stop_love / Stops spamming I love you 
delete_ksi / deletes the Lyrics
stop_sing / stop singing
sing / sing Thick Of it
coinflip / flip a coin
lock.gc / locks a gc
unlock.gc / unlocks a gc
diddyrate / check if user is diddy
nigger / kill a server 
status / Enables auto status
stop_status / Disables auto status
>911 / animate 911 attack
------------------------------------------
ANITOOL BY DJ
-------------
```
""",
"""
```
-----------------------------
[Message Commands]
-----------------------------
delete_msg / delete last msg
delete_all / delete all msg
-----------------------------
ANITOOL BY DJ
-----------------------------
```
""",
"""
````
-----------------------------
[Afk Commands]
-----------------------------
>afk (user) / Afk Check a user
>afk_stop / stops Afk checker
-----------------------------
ANITOOL BY DJ
------------------------------
```
"""]


    @commands.command()
    async def help(self, ctx):
        """Displays the help message."""
        try:
            self.bot.logger.info("Help requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[0])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")
    
    @commands.command(name="search-packing")
    async def search_packing(self, ctx):
        """Displays the help message for packing commands."""
        try:
            self.bot.logger.info("search packing requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[1])
        
        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")
    
    @commands.command(name="search-response")
    async def search_response(self, ctx):
        """Displays the help message for auto response commands."""
        try:
            self.bot.logger.info("search response requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[2])
        
        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command(name="search-gc")
    async def search_gc(self, ctx):
        """Displays the help message for gc commands."""
        try:
            self.bot.logger.info("search gc requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[3])
        
        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command(name="search-reactions")
    async def search_reactions(self, ctx):
        """Displays the help message for reactions commands."""
        try:
            self.bot.logger.info("search reactions requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[4])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command(name="search-spam")
    async def search_spam(self, ctx):
        """Displays the help message for spam commands."""
        try:
            self.bot.logger.info("search spam requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[5])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    
    @commands.command(name="search-info")
    async def help_info(self, ctx):
        """Displays the help message for info commands."""
        try:
            self.bot.logger.info("search info requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[6])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")    

    @commands.command(name="search-admin")
    async def search_admin(self, ctx):
        """Displays the help message for admin commands."""
        try:
            self.bot.logger.info("search admin requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[7])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")
    
    @commands.command(name="search-misc")
    async def search_misc(self, ctx):
        """Displays the help message for misc commands."""
        try:
            self.bot.logger.info("search misc requested.")
            await ctx.message.delete()
            await ctx.send(self.HELPLIST[8])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command(name="search-more")
    async def search_more(self, ctx):
        """Displays the help message for more commands."""
        try:
           self.bot.logger.info("search more requested.")
           await ctx.message.delete()
           await ctx.send(self.HELPLIST[9])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command(name="search-msg")
    async def search_msg(self, ctx):
        """Displays the help message for mag commands."""
        try:
           self.bot.logger.info("search more requested.")
           await ctx.message.delete()
           await ctx.send(self.HELPLIST[10])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")

    @commands.command(name="search-afk")
    async def search_msg(self, ctx):
        """Displays the help message for afk commands."""
        try:
           self.bot.logger.info("search more requested.")
           await ctx.message.delete()
           await ctx.send(self.HELPLIST[11])

        except Exception as e:
            self.bot.logger.error(f"An error occurred: {e}")


async def setup(bot):
    await bot.add_cog(HelpCog(bot))