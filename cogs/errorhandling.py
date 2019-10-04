from discord.ext import commands
import traceback
import discord
import json
import sys

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dev = None
        self.config = json.load(open('config.json'))
        self.debug = self.config['debug'] if 'debug' in self.config else False
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.dev = self.bot.get_user(self.bot.owner_id)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound, commands.CheckFailure) #Ignore these errors as they're not important
        permissionerr = (commands.BotMissingPermissions, commands.MissingPermissions, discord.Forbidden) #Permission related errors, so that the original message can be sent
        nodetails = (KeyError, AttributeError) #Don't provide much details about Python exceptions
        nodm = (commands.BadArgument, commands.MissingRequiredArgument) #Don't DM the developer for these
        
        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        if isinstance(error, permissionerr):
            #If it's permission related, send the error which will include the missing permissions or error code
            return await ctx.send(f'⁉ {error}')

        elif isinstance(error, ignored): 
            #If it's ignored, do nothing.
            return
        

        elif isinstance(error, nodetails):
            #If it's a Python error, just give a generic message as the message it gives won't help the user
            await ctx.send('⁉ Something went wrong and the developer has been notified.')
            tb = ''.join(traceback.format_exception(type(error), error, error.__traceback__)) # Get the traceback to help the developer
            embed = discord.Embed(title='An error occured', description=f'```py\n{tb}\n```', color=discord.Color.red())
            embed.add_field(name='User', value=f'{ctx.author} ({ctx.author.id})', inline=False)
            embed.add_field(name='Guild', value=ctx.guild.name or 'Direct Message', inline=False)
            embed.add_field(name='Message', value=ctx.message.content, inline=False)
            return await self.dev.send(embed=embed)

        else:
            await ctx.send(f'⁉ {error}')
            if not isinstance(error, nodm):
                tb = ''.join(traceback.format_exception(type(error), error, error.__traceback__)) # Get the traceback to help the developer
                embed = discord.Embed(title='An error occured', description=f'```py\n{tb}\n```', color=discord.Color.red())
                embed.add_field(name='User', value=f'{ctx.author} ({ctx.author.id})', inline=False)
                embed.add_field(name='Guild', value=ctx.guild.name or 'Direct Message', inline=False)
                embed.add_field(name='Message', value=ctx.message.content, inline=False)
                return await self.dev.send(embed=embed)


    @commands.command()
    async def debug(self, ctx, debug: bool = False):
        if ctx.author.id == self.dev.id:
            if not debug:
                self.config['debug'] == False
                self.debug = False
                with open('config.json', 'w') as f:
                    json.dump(self.config, f, indent=2)
                await ctx.send('Successfully disabled debug mode. Errors will not be sent to you.')
            else:
                self.config['debug'] == True
                self.debug = True
                with open('config.json', 'w') as f:
                    json.dump(self.config, f, indent=2)
                await ctx.send('Successfully enabled debug mode. Errors will be sent to you.')

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))