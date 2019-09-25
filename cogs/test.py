import discord
from discord.ext import commands


class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='test')
    async def _test(self, ctx, username: discord.Member = None):


def setup(bot):
    bot.add_cog(test(bot))