import discord
from discord.ext import commands


class Sample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sample2")
    async def command(self, ctx, arg1="sample2arg"):
        async with ctx.typing():

            embed = discord.Embed(
                title="Sample 2 Text",
                description=arg1,
                color=discord.Color(0xFFFFFF),
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Sample(bot))
