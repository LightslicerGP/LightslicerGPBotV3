import discord
from discord.ext import commands
import io

# done 10/2/24
# done again 12/15/25


class Banlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="banlist",
        aliases=["banned"],
        help="Shows a list of all banned users in this server.",
        description="Displays the server's ban list, including user IDs and reasons if available.",
    )
    async def banlist(self, ctx):
        async with ctx.typing():
            ban_list = []
            file_lines = []

            async for entry in ctx.guild.bans():
                ban_list.append(f"{entry.user} `({entry.user.id})` - {entry.reason}")
                file_lines.append(f"{entry.user.id} - {entry.user} - {entry.reason}")

            embed = discord.Embed(
                title="Banned Users",
                description=(
                    "\n".join(ban_list) if ban_list else "No banned users found."
                ),
                color=discord.Color(0x80BFFF),
            )

            file = discord.File(
                io.StringIO("\n".join(file_lines)), filename="banned_users.txt"
            )

        await ctx.reply(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(Banlist(bot))
