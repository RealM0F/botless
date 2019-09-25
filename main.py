from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import discord
import json

extensions = [
    "cogs.echo",
    "cogs.ban",
    "cogs.kick",
    "cogs.whois",
    "cogs.github",
    "cogs.archwiki",
    "cogs.blockgame",
    "cogs.errorhandling",
    "jishaku"
]

bot = commands.Bot(command_prefix="$", status=discord.Status.idle, activity=discord.Game(name="Starting..."), case_insensitive=True)

# Loading configuration file
config = json.load(open('config.json'))

for cog in extensions:
    try:
        bot.load_extension(cog)
        print(f"{cog} has been loaded")
    except Exception:
        print(f"Error while loading {cog}")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Ready!"))

bot.run(config['token'])