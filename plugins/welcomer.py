import discord,requests
import os
from discord.ext import commands
import random
from io import BytesIO
from datetime import datetime

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        backgrounds = [
            "stars",
            "stars2",
            "rainbowgradient",
            "rainbow",
            "sunset",
            "night",
            "blobday",
            "blobnight",
            "space",
            "gaming1",
            "gaming3",
            "gaming2",
            "gaming4",
        ]
        bgtype = random.randint(1, 7)
        # Chane in r the guildName as your guild urlencoded name!
        r = requests.get(
            f"https://some-random-api.ml/welcome/img/{bgtype}/{random.choice(backgrounds)}?type=join&username={member.name}&discriminator={member.discriminator}&avatar={member.avatar}&guildName=Baracchino%20Della%20Scuola&textcolor=white&memberCount={len(member.guild.members)}&key={os.environ.get('API_KEY')}"
        )
        """
        emb.set_thumbnail(url="https://i.imgur.com/R1KuVAG.png")
        emb.set_author(name=member, icon_url=member.avatar)
        emb.timestamp = datetime.now()
        """
        ch = self.bot.get_channel(int(os.environ.get("WELCOME_LEAVE")))
        image_binary = BytesIO(r.content)
        await ch.send(file=discord.File(fp=image_binary, filename="image.png"))
        # await ch.send(embed=emb)
        # await ch.send(r.content)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("Uscito")
        backgrounds = [
            "stars",
            "stars2",
            "rainbowgradient",
            "rainbow",
            "sunset",
            "night",
            "blobday",
            "blobnight",
            "space",
            "gaming1",
            "gaming3",
            "gaming2",
            "gaming4",
        ]
        bgtype = random.randint(1, 7)
        r = requests.get(
            f"https://some-random-api.ml/welcome/img/{bgtype}/{random.choice(backgrounds)}?type=leave&username={member.name}&discriminator={member.discriminator}&avatar={member.avatar}&guildName=Baracchino%20Della%20Scuola&textcolor=white&memberCount={len(member.guild.members)}&key={os.environ.get('API_KEY')}"
        )

        emb = discord.Embed(
            title=f"{member} è uscito!",
            description=f"Speriamo che {member.mention} torni.",
            color=discord.Color.brand_red(),
        )
        emb.set_thumbnail(url="https://i.imgur.com/R1KuVAG.png")
        emb.set_author(name=member, icon_url=member.avatar)
        emb.timestamp = datetime.now()
        image_binary = BytesIO(r.content)
        ch = self.bot.get_channel(int(os.environ.get("WELCOME_LEAVE")))
        await ch.send(file=discord.File(fp=image_binary, filename="image.png"))


async def setup(bot):
    print("To load welcomer, make sure to have set API_KEY in manager envoirnement variables to a some-ranom-api.ml key!")
    await bot.add_cog(Welcomer(bot))
