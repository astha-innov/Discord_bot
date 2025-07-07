import requests
from discord.ext import commands


class Fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fun_fact(self, ctx):
        response = requests.get('https://uselessfacts.jsph.pl/random.json')
        data = response.json()
        await ctx.send(f'{data['text']}')


async def setup(bot):
    await bot.add_cog(Fact(bot))
