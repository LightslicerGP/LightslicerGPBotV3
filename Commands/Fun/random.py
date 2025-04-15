import discord
from discord.ext import commands
import random

# done 10/1/24


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="random")
    async def command(self, ctx, arg1=0, arg2=1000):
        async with ctx.typing():

            embed = discord.Embed(
                title="And your number is...",
                description=str(random.randint(int(arg1), int(arg2))),
                color=discord.Color(0xFFFFFF),
            ).set_footer(
                text="usage []=optional: #random [lower (default = 0)] [higher (default = 1000)]"
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Random(bot))
