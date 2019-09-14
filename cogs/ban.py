import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='ban')
    @has_permissions(ban_members=True)
    async def _ban(self, ctx, member: discord.Member = None, arg = None):
        if member:
            if arg:
                await ctx.message.delete()
                await ctx.guild.kick(user=member, reason=f"{member} got banned by {ctx.author.name} because {arg}")
                await ctx.send(f'{member} got banned because {arg} :sunglasses:')
            else:
                await ctx.message.delete()
                await ctx.guild.ban(user=member, reason=f"Banned by: {ctx.author.name}")
                await ctx.send(f'{member} has been banned. :sunglasses:')
        else:
            await ctx.send(f'Invalid user.')

def setup(bot):
    bot.add_cog(ban(bot))