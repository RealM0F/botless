import discord
from discord.ext import commands

import aiohttp
import asyncio 
import json
import re

class archwiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot        

    @commands.command(name='archwiki')
    async def _archwiki(self, ctx, *, arg = None):
        if arg:
            yeet = re.sub(" ", "%20", arg)
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://wiki.archlinux.org/api.php?action=opensearch&format=json&formatversion=2&search={yeet}&namespace=0&limit=5&suggest=true') as ae:
                    e = await ae.json()
                    status = ae.status
                    #
                    # Check if the arch wiki responded correctly.
                    #
                    if status != 200:
                        ctx.send(f"Something went wrong. Errorcode: {status}")
                    else:
                        if e[3]:
                            embed = discord.Embed()
                            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Archlinux-icon-crystal-64.svg/2000px-Archlinux-icon-crystal-64.svg.png")
                            embed.add_field(name="Results:", value=re.sub(r"\[|\]|\,|\'", " ", str(e['3'])), inline=True)
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed()
                            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Archlinux-icon-crystal-64.svg/2000px-Archlinux-icon-crystal-64.svg.png")
                            embed.add_field(name="Results:", value=f"There's nothing on the arch wiki about {arg}", inline=True)
                            await ctx.send(embed=embed)

        else:
            await ctx.send(f"Invalid argument!", delete_after=5)

def setup(bot):
    bot.add_cog(archwiki(bot))