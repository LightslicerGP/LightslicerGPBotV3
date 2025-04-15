import discord
from discord.ext import commands
import requests

# done 10/1/24
# to do, check if it works 4/15/25

api_token = 0


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chat")
    async def command(self, ctx, arg1="sample2arg"):
        async with ctx.typing():

            if arg1:
                message = arg1.replace(" ", "%20")
                response = requests.get(
                    f"https://api.some-random-api.com/chatbot?key={api_token}&message={message}"
                ).json()
                embed = discord.Embed(
                    title="LightslicerGPBot responds:",
                    description=response.get("response", "false response given, sad"),
                    color=discord.Color(0xFFFF80),
                )
            else:
                embed = discord.Embed(
                    title="Please include some text for the bot to reply to!!",
                    color=discord.Color(0xFFFF80),
                )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Chat(bot))
