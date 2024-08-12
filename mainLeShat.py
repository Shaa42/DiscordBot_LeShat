import discord
from discord.ext import commands

#Token du bot
from tokenBot import LESHAT_TOKEN

# Créez un objet Intents et activez ceux dont vous avez besoin
intents = discord.Intents.default()
intents.presences = True 
intents.message_content = True  # Assurez-vous que cela est activé pour pouvoir lire les contenus des messages
intents.members = True  # Activez cela si vous avez besoin de gérer les événements de membres


#Préfixe du bot 
bot = commands.Bot(command_prefix = "meow ", intents = intents)

# Event du bot 
# Message lancement du bot
@bot.event
async def on_ready():
    print(f"Meow ! ({bot.user} s'est connecté !)")
    
    # Chargement des cogs
    await bot.load_extension('serverMember')
    print("ServerMemberCog : ok.")

# Gestion global des erreurs
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound): # Si commande n'existe pas
        await ctx.send('Cette commande n\'existe pas.')
        print("Un couillon à essayé une commande.")
    # else: # Si autre erreur survenue
    #     await ctx.send('Je sais pas ce qui s\'est passé frère')

# réagit à chaque message contenant "meow"
@bot.event
async def on_message(message):
    # Evite les loop avec le bot lui même
    if message.author == bot.user:
        return
    
    # Ajoute une réaction si le message contient "meow"
    if ('meow' in message.content.lower()) or ('cat' in message.content.lower()):
        await message.add_reaction('🐱')

    # Permet de quand meme process la commande
    await bot.process_commands(message)


# Commandes du bot
# Commande de base pour test
@bot.command()
async def boum(ctx):
    """
    allah uakbar
    """
    await ctx.send('Ta grand mère qui explose et miaule.')
    
    
    
"""
Commande pour dire bonjour à la personne
"""
@bot.command()
async def hello(ctx, name : str):
    """
    Ca te dit bonjour.
    """
    
    if name == "tobi":
        await ctx.send(f'Tobite.')
    else:
        await ctx.send(f'Hello {name}, tu es une bonne personne.')
# Gestion d'erreur pour : Hello
@hello.error
async def Hello_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Met un nom couillon. Syntaxe: `meow Hello <name>`')



"""
Commande pour faire des additions
"""
@bot.command()
async def sum(ctx, int1 : int, int2 : int):
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

    
#Run le bot
bot.run(LESHAT_TOKEN)
    