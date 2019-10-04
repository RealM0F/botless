import discord
from discord.ext import commands
from discord import Spotify

class spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(name='spotify')
    async def _spotify(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid argument.")

    @_spotify.command()
    async def lyrics(self, ctx, username: discord.Member = None):
            
        print(username)
        print(username.activity.title)
        
        if username.activity.name is 'Spotify':
            await ctx.send("user is playing spotify")
        else:
            await ctx.send(f"{username} is not using spotify.")
                

def setup(bot):
    bot.add_cog(spotify(bot))