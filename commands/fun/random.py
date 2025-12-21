import discord
from discord.ext import commands
import random

# done 10/1/24
# done again 12/15/25


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="random")
    async def random(self, ctx, lower: int = 1, upper: int = 100):
        async with ctx.typing():
            number = random.randint(lower, upper)

            embed = discord.Embed(
                title="And your number is...",
                description=str(number),
                color=discord.Color(0x80BFFF),
            ).set_footer(
                text="usage []=optional: #random [lower (default = 1)] [upper (default = 100)]"
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Random(bot))
