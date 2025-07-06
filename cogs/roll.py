from discord.ext import commands
import random


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx):
        number = random.randint(1, 6)
        await ctx.send(f'🎲 You rolled a {number} !')


async def setup(bot):
    await bot.add_cog(Dice(bot))
