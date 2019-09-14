import discord
from discord.ext import commands


class echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='echo')
    async def _echo(self, ctx, username: discord.Member):
        await ctx.send(username.activity.spotify)


def setup(bot):
    bot.add_cog(echo(bot))