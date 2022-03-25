import discord
from discord.ext import commands
import requests

_carbon_url = "https://carbonnowsh.herokuapp.com/"


def code_to_url(code: str) -> str:
    return f"{_carbon_url}?&code={trim_url(encode_url(code))}"


class Carbon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def carbonate(self, ctx, *, code):

        carbon_url = code_to_url(code)
        r = requests.get(carbon_url)

        b = BytesIO(r.content)
        await ctx.send(file=discord.File(fp=b, filename="code.png"))


def setup(bot):
    bot.add_cog(Carbon(bot))
