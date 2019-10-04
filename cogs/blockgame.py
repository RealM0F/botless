import discord
from discord.ext import commands

import aiohttp
import asyncio
import json
import re
import time

class blockgame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hyperium')
    async def _hyperium(self, ctx, arg = None):
        if arg:
            hello = {
	        'USER-AGENT': 'Botless (Python 3.7.4 / aiohttp 3.5.4) | Botless Discord Bot',
	        'CONTENT-TYPE': 'application/json' 
            }
            async with aiohttp.ClientSession(headers=hello) as session:
                async with session.get(f'https://api.sk1er.club/purchases/{arg}') as memes:
                    purchases = await memes.json()
                    status = memes.status
                    if status != 200:
                        raise commands.CommandError(f'Sk1er\'s API responded with {status}')
                    
                    try:
                        embed = discord.Embed()
                        embed.set_thumbnail(url="https://avatars1.githubusercontent.com/u/36334560?s=200&v=4")
                        embed.add_field(name="Hyperium credits:", value=purchases['remaining_credits'], inline=True)
                        assbath = re.sub(r"\[|\]|\_|\'", " ", str(purchases['hyperium'])).lower().title()
                        embed.add_field(name="Hyperium cosmetics:", value=assbath, inline=True)    
                        await ctx.send(embed=embed)
                    
                    except Exception as e:
                        raise commands.CommandError('Something went wrong while fetching the info')

    @commands.command(name='hypixel')
    async def _hypixel(self, ctx, arg = None):
        header = {
	    'USER-AGENT': 'Botless (Python 3.7.4 / aiohttp 3.5.4) | Botless Discord Bot',
	    'CONTENT-TYPE': 'application/json'
        }
        if arg:
            async with aiohttp.ClientSession(headers=header) as session:
                async with session.get(f'https://api.sk1er.club/player/{arg}') as userinfo:
                    info = await userinfo.json()
                    status = userinfo.status
                    
                    if status != 200: 
                        raise commands.CommandError(f'Sk1er\'s API responded with {status}')
                    try:
                        embed = discord.Embed()
                        embed.set_thumbnail(url="https://i.imgur.com/f85vTZT.png")
                        embed.add_field(name="Username:", value=info['player']['playername'], inline=True)
                        embed.add_field(name="UUID:", value=info['player']['uuid'], inline=True)
                        
                        hypixelrank = {
                        'NONE': 'No rank',
                        'VIP': 'VIP',
                        'VIP_PLUS': 'VIP+',
                        'MVP': 'MVP',
                        'MVP_PLUS': 'MVP+',
                        'MVP_PLUS_PLUS': 'MVP++'
                        }
                        embed.add_field(name="Rank:", value=hypixelrank[str(info['player']['rank_for_mod'])], inline=False)
                        
                        # Convert epoch time into a human readable format + make this code kind of readable
                        firstlog = time.strftime('%d.%m.%Y', time.localtime(info['player']['firstLogin'] / 1000))
                        lastlog = time.strftime('%d.%m.%Y', time.localtime(info['player']['lastLogin'] / 1000))
                        embed.add_field(name="Last login:", value=lastlog, inline=True)
                        embed.add_field(name="First login:", value=firstlog, inline=True)

                        embed.add_field(name="Last played version:", value=info['player']['mcVersionRp'], inline=True)
                        embed.add_field(name="Last played minigame:", value=info['player']['mostRecentGameType'], inline=True)
                        await ctx.send(embed=embed)
                    except Exception:
                        raise commands.CommandError('Something went wrong while fetching the info')
def setup(bot):
    bot.add_cog(blockgame(bot))