import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='Kick')
    @has_permissions(kick_members=True)
    async def _kick(self, ctx, member: discord.Member):
        if member:
            if arg:
                await ctx.message.delete()
                await ctx.guild.kick(user=member, reason=f"{member} got kicked by {ctx.author.name} because {arg}")
                await ctx.send(f'{member} got kicked by {ctx.author.name} because {arg}')
            else:
                await ctx.message.delete()
                await ctx.guild.kick(user=member, reason=f"{member} got kicked by {ctx.author.name}")
                await ctx.send(f'{member} has been kicked.')
        else:
            await ctx.send(f'Invalid user.')

def setup(bot):
    bot.add_cog(kick(bot))