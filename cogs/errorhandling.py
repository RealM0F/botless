import traceback
import sys
from discord.ext import commands
import discord

#
# Source: https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
#

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = (commands.CommandNotFound)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, discord.ext.commands.errors.BadArgument):
            await ctx.send('Invalid argument.')

        #elif isinstance(error, InvalidData):
        #    await ctx.send('Oh god. Discord is breaking down.')

#
# To do: 
# Make it show the stacktrace when there is a actual problem
#

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))