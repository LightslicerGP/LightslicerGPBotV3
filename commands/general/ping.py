import discord
from discord.ext import commands

# done 10/1/24
# done again 12/15/25


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        async with ctx.typing():
            latency = round(self.bot.latency * 1000)
            embed = discord.Embed(
                title="Pong!",
                description=f"Latency: {latency}ms",
                color=discord.Color(0x80BFFF),
            )
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Ping(bot))
