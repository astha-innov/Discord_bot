import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.getenv('test_bot_token')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')


@bot.command()
async def greet(ctx):
    await ctx.send('Hellooo Senpai 🤗')


async def main():
    await bot.load_extension('cogs.roll')
    await bot.load_extension('cogs.joke')
    await bot.load_extension('cogs.quote')
    await bot.load_extension('cogs.fun_fact')


asyncio.run(main())
bot.run(Token)
