from discord.ext import commands

class MathOperations(commands.Cog):
    """
    Allow user to do math
    """
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # Somme
    @commands.command()
    async def sum(self, ctx, int1 : int, int2 : int):
        """
        fait une addition, en gros.
        """
        somme = int1 + int2
        await ctx.send(f"{int1} + {int2} = {somme}")
    #Gestion d'erreur pour : sum
    @sum.error
    async def sum_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Syntaxe: `meow sum <nombre1> <nombre2>`')
            
            
            
    # Multiplication
    @commands.command()
    async def mul(self, ctx, int1 : int, int2 : int):
        """
        fait une multiplication, en gros.
        """
        mul = int1 * int2
        await ctx.send(f"{int1} x {int2} = {mul}")
    # Gestion d'erreur pour : mul
    @sum.error
    async def sum_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Syntaxe: `meow mul <nombre1> <nombre2>`')
            
            
            
    # Division

# Initialisation du cog : MathOperations
async def setup(bot):
    await bot.add_cog(MathOperations(bot))