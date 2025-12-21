import discord
from discord.ext import commands
import urllib.parse

# done 12/15/25


class Comment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="comment")
    async def comment(self, ctx, *, message: str = None):
        if not message:
            await ctx.reply(
                embed=discord.Embed(
                    title="Missing Text",
                    description="Please include some text to put in the comment!",
                    color=discord.Color(0xFFFF80),
                )
            )
            return

        async with ctx.typing():
            user = ctx.author
            username = urllib.parse.quote_plus(user.name[:15])
            avatar = urllib.parse.quote_plus(user.display_avatar.url)
            comment = urllib.parse.quote_plus(message)

            url = (
                "https://api.some-random-api.com/canvas/misc/youtube-comment"
                f"?username={username}"
                f"&avatar={avatar}"
                f"&comment={comment}"
            )

            embed = discord.Embed(
                title="Here is your comment",
                description="Enjoy!",
                color=discord.Color(0xFFFF80),
            ).set_image(url=url)

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Comment(bot))
