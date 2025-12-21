import discord
from discord.ext import commands
import random

# done 10/1/24
# done again 12/15/25


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coinflip", aliases=["flip"])
    async def coinflip(self, ctx):
        async with ctx.typing():
            roll = random.randint(1, 1001)

            if roll == 1:
                description = (
                    "***The coin somehow landed on its edge. "
                    "I don’t know how. I don’t make the rules. "
                    "You just hit a 1/1001 chance. Be proud.***"
                )
            elif roll <= 501:
                description = "Heads"
            else:
                description = "Tails"

            embed = discord.Embed(
                title="And you flipped…",
                description=description,
                color=discord.Color(0x80BFFF),
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Coinflip(bot))
