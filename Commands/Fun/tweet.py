import discord
from discord.ext import commands
import requests

# 10/1/24 technically done, but api supports custom counts
# and theme, add that as like --theme=dark or whatever idk


class Tweet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tweet")
    async def command(self, ctx, *, comment=None):
        async with ctx.typing():
            if not comment:
                embed = discord.Embed(
                    title="Please include some text to put in the tweet!",
                    color=discord.Color(0xFFFFFF),
                )
            else:
                user = ctx.author
                username = user.name[:15]
                displayname = user.display_name
                avatar = user.avatar.url
                message = comment.replace(" ", "%20")

                url = f"https://api.some-random-api.com/canvas/tweet?username={username}&displayname={displayname}&avatar={avatar}&comment={message}"
                embed = discord.Embed(
                    title="Here is your tweet",
                    description="Enjoy!",
                    color=discord.Color(0xFFFFFF),
                ).set_image(url=url)

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Tweet(bot))
