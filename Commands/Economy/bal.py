import discord
from discord.ext import commands
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    token = config["token"]
    api_token = config["apiToken"]

# TO DO 4/15/25

class Bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Bal")
    async def command(self, ctx, arg1="sample2arg"):
        async with ctx.typing():

            embed = discord.Embed(
                title="{} has ${}",
                description=arg1,
                color=discord.Color(0x80FF80),
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Bal(bot))
