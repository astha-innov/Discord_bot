from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def senpai_help(self, ctx):
        help_text = '''
        **Senpai Commands 🤖:**
    `/greet` - says **'Hellooo Senpai 🤗'**
    `/joke`  - tells a random joke
    `/quote` - shares a motivational quote
    `/roll`  - rolls a dice in range(1, 6)
    `/fun_fact` - sends a random bizarre fact
    '''
        await ctx.send(help_text)


async def setup(bot):
    await bot.add_cog(Help(bot))
