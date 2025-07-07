import requests
from discord.ext import commands


class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        response = requests.get(' https://zenquotes.io/api/random')
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        await ctx.send(f'{quote} - {author}')


async def setup(bot):
    await bot.add_cog(Quote(bot))
