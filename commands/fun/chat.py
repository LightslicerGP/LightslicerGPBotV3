import discord
from discord.ext import commands
import requests
import urllib.parse
import json

# done 10/1/24
# to do, check if it works 4/15/25
# done, might change to use nvidia free api idk 12/15/25

CONFIG_FILE = "config.json"


def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


config = load_config()
API_TOKEN = config.get("SRAToken")


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chat")
    async def chat(self, ctx, *, message: str = "sample2arg"):
        async with ctx.typing():
            if message:
                encoded_message = urllib.parse.quote_plus(message)
                url = f"https://api.some-random-api.com/chatbot?key={API_TOKEN}&message={encoded_message}"
                # print(url)
                response = requests.get(url).json()

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
