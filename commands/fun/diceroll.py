import discord
from discord.ext import commands
import random

# done 12/15/25


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Shared roll logic
    async def do_roll(self, ctx):
        async with ctx.typing():
            value = random.randint(1, 6)

            embed = discord.Embed(
                title="Dice Roll",
                description=f"You rolled a **{value}**!",
                color=discord.Color(0x80BFFF),
            )

        await ctx.send(embed=embed)

    # #dice roll
    @commands.group(invoke_without_command=True)
    async def dice(self, ctx):
        await ctx.send("Use `#dice roll` or `#diceroll` to roll a dice")

    @dice.command()
    async def roll(self, ctx):
        await self.do_roll(ctx)

    # #diceroll
    @commands.command(name="diceroll")
    async def dice_roll(self, ctx):
        await self.do_roll(ctx)


async def setup(bot):
    await bot.add_cog(Dice(bot))
