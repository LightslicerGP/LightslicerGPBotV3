import discord
from discord.ext import commands
import os, sys, json, time, platform

# started 10/3/24, need to add hyperlink to owner and a
# ton of other info still.
# above was about bot info, done 12/15/25

OWNER_ID = 586225258269245538
RESTART_STATE_FILE = "restart_state.json"


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    # Shared restart logic
    async def do_restart(self, ctx):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You are not allowed to restart the bot!",
                color=discord.Color(0x80BFFF),
            )
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(
            title="Restarting Bot",
            description="The bot is restarting now...",
            color=discord.Color(0x80BFFF),
        )

        msg = await ctx.send(embed=embed)

        # ✅ Save restart context
        with open(RESTART_STATE_FILE, "w") as f:
            json.dump(
                {
                    "channel_id": msg.channel.id,
                    "message_id": msg.id,
                },
                f,
            )

        await self.bot.close()
        os.execv(sys.executable, [sys.executable] + sys.argv)

    # #bot
    @commands.group(invoke_without_command=True)
    async def bot(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
                title="Available subcommands",
                description="restart\ninfo",
                color=discord.Color(0x80BFFF),
            )
            await ctx.send(embed=embed)

    # #bot restart
    @bot.command()
    async def restart(self, ctx):
        await self.do_restart(ctx)

    # #restart
    @commands.command(name="restart")
    async def restart_shortcut(self, ctx):
        await self.do_restart(ctx)

    # #bot info
    @bot.command(name="info")
    async def info(self, ctx):
        async with ctx.typing():
            now = time.time()
            uptime_seconds = int(now - self.start_time)

            days, remainder = divmod(uptime_seconds, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            uptime = f"{days}d {hours}h {minutes}m {seconds}s"

            app_info = await self.bot.application_info()

            embed = discord.Embed(
                title="Bot Information",
                color=discord.Color(0x80BFFF),
            )

            embed.set_thumbnail(url=self.bot.user.display_avatar.url)

            embed.add_field(name="Name", value=self.bot.user.name, inline=True)
            embed.add_field(name="ID", value=self.bot.user.id, inline=True)
            embed.add_field(name="Mention", value=self.bot.user.mention, inline=True)

            embed.add_field(name="Owner", value=f"<@{app_info.owner.id}>", inline=True)
            embed.add_field(name="Verified", value=app_info.bot_public, inline=True)
            embed.add_field(name="Guilds", value=len(self.bot.guilds), inline=True)

            embed.add_field(
                name="Users",
                value=sum(g.member_count or 0 for g in self.bot.guilds),
                inline=True,
            )

            embed.add_field(
                name="Commands",
                value=len(self.bot.commands),
                inline=True,
            )

            embed.add_field(
                name="Latency",
                value=f"{round(self.bot.latency * 1000)} ms",
                inline=True,
            )

            embed.add_field(name="Uptime", value=uptime, inline=False)

            embed.add_field(
                name="Python",
                value=platform.python_version(),
                inline=True,
            )

            embed.add_field(
                name="discord.py",
                value=discord.__version__,
                inline=True,
            )

            embed.add_field(
                name="Platform",
                value=f"{platform.system()} {platform.release()}",
                inline=True,
            )

            embed.add_field(
                name="Process ID",
                value=os.getpid(),
                inline=True,
            )

            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Bot(bot))
