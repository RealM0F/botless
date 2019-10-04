import discord
from discord.ext import commands

import aiohttp
import asyncio 
import json

class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='github')
    async def _github(self, ctx):
        if ctx.invoked_subcommand is None:
            raise commands.BadArgument('Invalid argument')

    @_github.command()
    async def user(self, ctx, arg1 = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.github.com/users/{arg1}') as ae:
                e = await ae.json()
                status = ae.status
                if status == 200:
                    embed = discord.Embed()
                    embed.set_thumbnail(url=(e['avatar_url']))
                    embed.add_field(name="Name:", value=f"[{e['login']}]({e['html_url']})", inline=True)
                    embed.add_field(name="Email", value=e['email'], inline=True)
                    embed.add_field(name="Bio:", value=e['bio'], inline=False)
                    embed.add_field(name="Location:", value=e['location'], inline=False)
                    embed.add_field(name="Public Repos:", value=e['public_repos'], inline=True)
                    embed.add_field(name="Public Gists:", value=e['public_gists'], inline=True)
                    embed.add_field(name="Created:", value=e['created_at'], inline=True)
                    embed.add_field(name="Updated:", value=e['updated_at'], inline=True)
                    await ctx.send(embed=embed)
                
                elif status == 404:
                    raise commands.BadArgument('Invalid User')
                
                else:
                    raise commands.CommandError(f'GitHub responded with the status {status}')

    @_github.command()
    async def org(self, ctx, arg1 = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.github.com/orgs/{arg1}') as ae:
                e = await ae.json()
                status = ae.status
                print(e)
                if status == 200:
                    embed = discord.Embed()
                    embed.set_thumbnail(url=(e['avatar_url']))
                    embed.add_field(name="Name:", value=f"[{e['login']}]({e['html_url']})", inline=True)
                    embed.add_field(name="Email", value=e['email'], inline=True)
                    
                    if e['description'] == "":
                        embed.add_field(name="Description:", value="Repo doesn't have a description", inline=False)
                    else:
                        embed.add_field(name="Description:", value=e['description'], inline=False)
                    #
                    # 
                    #
                    embed.add_field(name="Location:", value=e['location'], inline=False)
                    embed.add_field(name="Public Repos:", value=e['public_repos'], inline=True)
                    embed.add_field(name="Public Gists:", value=e['public_gists'], inline=True)
                    embed.add_field(name="Created:", value=e['created_at'], inline=True)
                    embed.add_field(name="Updated:", value=e['updated_at'], inline=True)                
                    await ctx.send(embed=embed)
                
                elif status == 404:
                    raise commands.BadArgument('Invalid organization')
                
                else:
                    raise commands.CommandError(f'GitHub responded with the status {status}')


def setup(bot):
    bot.add_cog(github(bot))