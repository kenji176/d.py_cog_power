from discord.ext import commands
from discord import app_commands
from io import BytesIO
import discord
import requests


class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.path = "https://weather.tsukumijima.net/api/forecast/city/"

    @commands.hybrid_command(name="天気予報", description="今日の天気がわかります")
    @app_commands.choices(住んでる地方=[
        app_commands.Choice(name="北海道地方", value="016010"),
        app_commands.Choice(name="関東地方", value="130010"),
        app_commands.Choice(name="東北地方", value='040010'),
        app_commands.Choice(name="中部地方", value='190010'),
        app_commands.Choice(name="近畿地方", value='270000'),
        app_commands.Choice(name="四国地方", value='370000'),
        app_commands.Choice(name="中国地方", value='340010'),
        app_commands.Choice(name="九州地方", value='430010'),
    ])
    async def weather(self, ctx, 住んでる地方: app_commands.Choice[str]):
        location = 住んでる地方
        res = requests.get(self.path+location.value)
        embed = discord.Embed(title=f"{location.name}の天気", description=res.json()['forecasts'][0]['telop'])
        embed.set_thumbnail(url=f"{res.json()['forecasts'][0]['image']['url'].replace('.svg','.png')}")
        embed.add_field(name="詳細", value=f"{res.json()['forecasts'][0]['detail']['weather']}", inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("weather")


async def setup(bot):
    await bot.add_cog(weather(bot))
