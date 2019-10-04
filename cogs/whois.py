import discord
from discord.ext import commands
from discord import Member


class whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='whois')
    async def _whois(self, ctx, *, username: discord.Member = None):
        if username != None:
            try:
                activity = username.activities[0]
            except IndexError:
                activity = None

            embed = discord.Embed(title=" ")
            
            embed.set_thumbnail(url=(username.avatar_url))
            embed.add_field(name="Username:", value=username, inline=True)
            embed.add_field(name="Status:", value=str(username.status).capitalize(), inline=True)
            embed.add_field(name="Joined at:", value=username.joined_at.strftime("%B %d %Y @ %H:%M:%S"), inline=True)
            embed.add_field(name="Created at:", value=username.created_at.strftime("%B %d %Y @ %H:%M:%S"), inline=True)
            
            actvtypes = {
            'ActivityType.playing': 'Playing:',
            'ActivityType.streaming': 'Streaming:',
            'ActivityType.listening': 'Listening to:'
            }

            if activity != None:
                embed.add_field(name=actvtypes[str(username.activities[0].type)], value=username.activity.name, inline=True)
            else:
                embed.add_field(name="RPC:", value=f"{username.name} has no RPC active!", inline=True)
                print("yes")
            
            embed.add_field(name="Bot:", value='Yes' if username.bot else 'No', inline=False)
            print(embed.to_dict())
            await ctx.send(embed=embed)
        else:
            raise commands.BadArgument('Invalid User')


def setup(bot):
    bot.add_cog(whois(bot))