from discord.ext import commands
import csv
from random import randint

class Anime(commands.Cog):
    """
    Anime commands
    """
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def rdanime(self, ctx):
        """
        renvoie un anime random
        """
        
        # 0 : anime_id
        # 1 : name
        # 2 : genre
        # 3 : type
        # 4 : episodes
        # 5 : rating
        # 6 : members
        
        with open("db/anime_db/anime.csv", newline='', encoding='utf-8') as anime_file:
            reader = csv.reader(anime_file, delimiter=',')
            lst_reader = list(reader)
            anime_hentai_free = []
            
            # Filtering, nb: "or" ne marche pas
            for row in lst_reader:
                genre = row[2]
                if ("Hentai" not in genre):
                    if ("Ecchi" not in genre):
                        if ("Yuri" not in genre):
                            if ("Yaoi" not in genre):
                                anime_hentai_free.append(row)
            
            lst_anime_size = len(anime_hentai_free)
            rd_seed = randint(0, lst_anime_size - 1)
            
            await ctx.send(anime_hentai_free[rd_seed][1])
            
        
# Initialisation du cog : Anime
async def setup(bot):
    await bot.add_cog(Anime(bot))