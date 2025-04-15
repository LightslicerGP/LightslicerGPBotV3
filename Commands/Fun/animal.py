import discord
from discord.ext import commands
import requests

# done 9/30/24


class Animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="animal")
    async def command(self, ctx, animal="None"):
        async with ctx.typing():
            if animal.lower() in ["dog", "cat", "bird", "fox", "koala", "panda"]:
                animal = animal.lower()
                response = requests.get(
                    f"https://api.some-random-api.com/animal/{animal}"
                ).json()
                embed = discord.Embed(
                    title=f"Here is your {animal} picture and fact!",
                    description=response.get("fact", f"rip theres no {animal} fact"),
                    color=discord.Color(0xFFFF80),
                )
                embed.set_image(
                    url=response.get("image", f"rip theres no {animal} picture")
                )
            else:
                embed = discord.Embed(
                    title="List of animals you can do:\n- Dog\n- Cat\n- Bird\n- Fox\n- Koala\n- Panda",
                    description="Enjoy!",
                    color=discord.Color(0xFFFF80),
                )
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Animal(bot))
