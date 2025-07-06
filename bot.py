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


@bot.command()
async def inspire(ctx):
    await ctx.send("All the pain that doesn't kill you, will only make you stronger 🔥")


async def main():
    await bot.load_extension('cogs.roll')
    await bot.load_extension('cogs.joke')


asyncio.run(main())
bot.run(Token)
