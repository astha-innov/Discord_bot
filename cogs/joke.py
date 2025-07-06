import requests
from discord.ext import commands


class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        try:
            response = requests.get('https://v2.jokeapi.dev/joke/Any')
            data = response.json()
            if data['type'] == 'single':
                await ctx.send(data['joke'])
            else:
                await ctx.send(f"{data['setup']}\n{data['delivery']}")
        except Exception as e:
            await ctx.send("❌ Couldn't fetch a joke right now. Please try again later")


async def setup(bot):
    await bot.add_cog(Joke(bot))
