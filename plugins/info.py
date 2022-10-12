import discord
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.send("Bot created with discord bots creator")

async def setup(bot):
    await bot.add_cog(TestCog(bot))
