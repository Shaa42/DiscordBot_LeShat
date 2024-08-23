import discord
from discord.ext import commands

class ServerMember(commands.Cog):
    """
    Catégorie dédiée aux supra de FlexGang.
    """
    
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # Sarkymm
    @commands.command()
    async def Sarkymm(self, ctx):
        """sarkymm tribute"""
        await ctx.send('```\nSARKYMM LE GOAT RAAAAAAAAAAAAAAAAH\n```')
        
    # Sha
    @commands.command()
    async def Sha(self, ctx):
        """Papa ?"""
        await ctx.send('```\nLe papa du chat (meow).\n```')
        
    # Evoliosse
    @commands.command()
    async def Evoliosse(self, ctx):
        """T'as tout copaté"""
        await ctx.send('```\nPlease Riot nerf kata.\n```')
        
    @commands.command()
    async def Lucas(self, ctx):
        """Lucardo"""
        await ctx.send('```\nFan de foot\n```')
        
    @commands.command()
    async def Tomas(self, ctx):
        """Le goat imo."""
        await ctx.send("```\nPunpun enjoyer.\n```")
        
    @commands.command()
    async def Payn(self, ctx):
        """Le chef"""
        await ctx.send("```\nSukuna lover\n```")
        
    @commands.command()
    async def Zouhair(self, ctx):
        """Rab Sala"""
        await ctx.send("```\nZoubir\n```")
    
# Initialisation du cog : ServerMember
async def setup(bot):
    await bot.add_cog(ServerMember(bot))
        