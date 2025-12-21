import discord
from discord.ext import commands
import aiohttp

# done 9/30/24
# to do, new options 4/15/25
# done, even with new animals 12/15/25

ANIMALS = [
    "dog",
    "cat",
    "bird",
    "fox",
    "koala",
    "panda",
    "racoon",
    "birb",
    "red_panda",
    "kangaroo",
    "whale",
]

API_URL = "https://api.some-random-api.com/animal/{}"


class Animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="animal")
    async def animal(self, ctx, *, animal: str = None):
        async with ctx.typing():
            if animal:
                animal = animal.lower().replace(" ", "_")

            if animal and animal in ANIMALS:
                async with aiohttp.ClientSession() as session:
                    async with session.get(API_URL.format(animal)) as resp:
                        response = await resp.json()

                embed = discord.Embed(
                    title=f"Here is your {animal.replace('_', ' ')} picture and fact!",
                    description=response.get("fact", "No fact available."),
                    color=discord.Color(0xFFFF80),
                )
                embed.set_image(url=response.get("image", ""))

            else:
                embed = discord.Embed(
                    title="List of animals you can use:",
                    description="\n".join(
                        f"- {a.replace('_', ' ').title()}" for a in ANIMALS
                    ),
                    color=discord.Color(0xFFFF80),
                )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Animal(bot))
