import discord
from config import token
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def setup_hook():
    await bot.load_extension("cogs.weather")


@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Botがスタート')

if __name__ == "__main__":
    bot.run(token)
