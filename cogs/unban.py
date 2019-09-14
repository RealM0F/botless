import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


print("Did you really just load this?")

class unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='unban')
    @has_permissions(ban_members=True)
    async def _unban(self, ctx, user = None):
        if user:
            print("interesting")
            await ctx.guild.unban(user=user, reason=f"Unbanned by {ctx.author.name}")
        else:
            print("Invalid ID >:(")
def setup(bot):
    bot.add_cog(unban(bot))