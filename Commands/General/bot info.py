import discord
from discord.ext import commands
import time

# started 10/3/24, need to add hyperlink to owner and a
# ton of other info still.


class Bot_Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_start_time = time.time()

    @commands.group(name="bot", invoke_without_command=True)
    async def bot(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
                title="Send a subcommand:",
                description="For now: `#bot info`",
                color=discord.Color(0xFFFFFF),
            )
        await ctx.reply(embed=embed)

    @bot.command(name="info")
    async def info(self, ctx):
        async with ctx.typing():

            app_info = await self.bot.application_info()
            owner = app_info.owner

            creation_time = self.bot.user.created_at.strftime("%m/%d/%Y, %I:%M:%S %p")

            user_count = ctx.guild.member_count

            server_count = len(self.bot.guilds)

            total_commands = len(self.bot.commands)

            uptime = str(round(time.time() - self.bot_start_time))

            ping = round(self.bot.latency)
            message_ping = round(ctx.bot.latency * 1000)

            embed = (
                discord.Embed(
                    title="Bot Info",
                    description="Here is all the inormation you could possibly get from this, enjoy!",
                    color=discord.Color(0x80BFFF),
                )
                .add_field(name="Bot Owner", value=f"{owner}", inline=True)
                .add_field(
                    name="Bot Creation Date/Time", value=creation_time, inline=True
                )
                .add_field(name="User Count", value=f"`{user_count}`", inline=True)
                .add_field(name="Server Count", value=f"`{server_count}`", inline=True)
                .add_field(
                    name="Total Commands", value=f"`{total_commands}`", inline=True
                )
                .add_field(name="Uptime", value=uptime + " seconds", inline=True)
                .add_field(name="Bot Ping", value=f"`{ping}ms`", inline=True)
                .add_field(
                    name="Bot Database Ping",
                    value=f"uhhhh that doesnt exist on py version",
                    inline=True,
                )
                .add_field(
                    name="Bot Message Received Ping",
                    value=f"`{message_ping}ms`",
                    inline=True,
                )
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Bot_Info(bot))
