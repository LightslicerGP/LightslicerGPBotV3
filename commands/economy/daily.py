import discord
from discord.ext import commands
import json
import time

# done 12/15/25

DB_FILE = "database.json"


async def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


async def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)


DAILY_AMOUNT = 5000
COOLDOWN = 24 * 60 * 60  # 24 hours in seconds


class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        async with ctx.typing():
            db = await load_db()
            user_id = str(ctx.author.id)
            last_claim = db.get("Daily", {}).get(user_id, 0)
            now = int(time.time())

            if now - last_claim < COOLDOWN:
                remaining = COOLDOWN - (now - last_claim)
                hours = remaining // 3600
                minutes = (remaining % 3600) // 60
                seconds = remaining % 60
                embed = discord.Embed(
                    title="Daily Already Claimed",
                    description=f"Please wait {hours}h {minutes}m {seconds}s before claiming again.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            moneyDB = db.get("Money", {})
            moneyDB[user_id] = moneyDB.get(user_id, 0) + DAILY_AMOUNT
            db["Money"] = moneyDB

            dailyDB = db.get("Daily", {})
            dailyDB[user_id] = now
            db["Daily"] = dailyDB

            await save_db(db)

            embed = discord.Embed(
                title="Daily Claimed!",
                description=f"You received ${DAILY_AMOUNT:,}.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Daily(bot))
