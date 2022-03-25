import discord
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.send("Bot created with discord bots creator")

def setup(bot):
    bot.add_cog(TestCog(bot))