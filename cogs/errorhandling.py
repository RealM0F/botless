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
        ignored = (commands.CommandNotFound, commands.BadArgument)
        error1 = getattr(error, 'original', error)

        if isinstance(error1, ignored):
            return

        elif isinstance(error1, commands.CommandError):
            await ctx.send(error)
        
        elif isinstance(error1, commands.MissingPermissions):
            await ctx.send(f'Missing permissions in {ctx.channel}')


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))