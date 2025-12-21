import discord
from discord.ext import commands
import json
import asyncio

# done..? 12/19/25

OWNER_ID = 586225258269245538
DB_FILE = "database.json"

BUMP_CONFIRM_TEXT = "Bump done! :thumbsup:\nCheck it out [on DISBOARD](https://disboard.org/server/586543238589054997).\n\n\n*I develop and maintain this bot with dedication, with the support of amazing moderators and contributors behind the scenes.\nI cover all the costs myself — and to be honest, your support truly makes a difference.\nEven a small donation helps keep the bot going 💖\n🙏 Donate here: https://www.paypal.com/ncp/payment/V2257AKBQS2S6*"


async def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


async def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)


class Bump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Listener for DISBOARD bump confirmation
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Only process messages with embeds
        if not message.embeds:
            return

        embed = message.embeds[0]
        if embed.description != BUMP_CONFIRM_TEXT:
            return

        guild = message.guild
        if not guild:
            return

        # Get bump channel and bump role from db
        db = await load_db()
        channel_id = db.get("BumpChannel", {}).get(str(guild.id))
        role_id = db.get("BumpRole", {}).get(str(guild.id))

        if not channel_id or not role_id:
            return

        # Confirm bump and tell user you'll remind in 2 hours
        target_channel = guild.get_channel(int(channel_id))
        ping_role = guild.get_role(int(role_id))

        if not target_channel or not ping_role:
            return

        async with message.channel.typing():
            notify_embed = discord.Embed(
                title="Bump Scheduled",
                description="I'll remind you to bump again in 2 hours!",
                color=discord.Color(0x80BFFF),
            )
            await target_channel.send(embed=notify_embed)

        # Wait 2 hours, then ping the role in the bump channel
        await asyncio.sleep(2 * 60 * 60)
        await target_channel.send(f"{ping_role.mention} Time to bump again!")

    # #bump
    @commands.group(invoke_without_command=True)
    async def bump(self, ctx):
        embed = discord.Embed(
            title="Bump Commands",
            description=(
                "`#bump ping`\n"
                "`#bump channel`\n"
                "`#bump channel set (#channel)`\n"
                "`#bump role`\n"
                "`#bump role set (@role)`"
            ),
            color=discord.Color(0x80BFFF),
        )
        await ctx.reply(embed=embed)

    # #bump ping
    @bump.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Bump Ping",
            description="Waiting for the next DISBOARD bump confirmation…",
            color=discord.Color(0x80BFFF),
        )
        await ctx.reply(embed=embed)

    # #bump channel
    @bump.group(invoke_without_command=True)
    async def channel(self, ctx):
        db = await load_db()
        channel_id = db.get("BumpChannel", {}).get(str(ctx.guild.id))

        if not channel_id:
            desc = "No bump channel set."
        else:
            ch = ctx.guild.get_channel(int(channel_id))
            desc = ch.mention if ch else "Channel not found."

        await ctx.reply(
            embed=discord.Embed(
                title="Bump Channel",
                description=desc,
                color=discord.Color(0x80BFFF),
            )
        )

    # #bump channel set
    @channel.command(name="set")
    async def channel_set(self, ctx, channel: discord.TextChannel = None):
        if ctx.author.id != OWNER_ID:
            return await ctx.reply("You do not have permission.")

        if channel is None:
            channel = ctx.channel

        db = await load_db()
        db.setdefault("BumpChannel", {})[str(ctx.guild.id)] = str(channel.id)
        await save_db(db)

        await ctx.reply(
            embed=discord.Embed(
                title="Bump Channel Set",
                description=f"Channel set to {channel.mention}",
                color=discord.Color(0x80BFFF),
            )
        )

    # #bump role
    @bump.group(invoke_without_command=True)
    async def role(self, ctx):
        db = await load_db()
        role_id = db.get("BumpRole", {}).get(str(ctx.guild.id))

        if not role_id:
            desc = "No bump role set."
        else:
            role = ctx.guild.get_role(int(role_id))
            desc = role.mention if role else "Role not found."

        await ctx.reply(
            embed=discord.Embed(
                title="Bump Role",
                description=desc,
                color=discord.Color(0x80BFFF),
            )
        )

    # #bump role set
    @role.command(name="set")
    async def role_set(self, ctx, role: discord.Role):
        if ctx.author.id != OWNER_ID:
            return await ctx.reply("You do not have permission.")

        db = await load_db()
        db.setdefault("BumpRole", {})[str(ctx.guild.id)] = str(role.id)
        await save_db(db)

        await ctx.reply(
            embed=discord.Embed(
                title="Bump Role Set",
                description=f"Role set to {role.mention}",
                color=discord.Color(0x80BFFF),
            )
        )


async def setup(bot):
    await bot.add_cog(Bump(bot))
