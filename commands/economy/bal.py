import discord
from discord.ext import commands
import json
import random

# done 12/15/25

OWNER_ID = 586225258269245538
DB_FILE = "database.json"


async def load_money_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


async def save_money_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)


def format_money(amount):
    return f"{float(amount):,.2f}"


class Bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # #bal
    @commands.group(invoke_without_command=True, aliases=["balance"])
    async def bal(self, ctx, member: discord.Member = None):
        async with ctx.typing():
            if member is None:
                member = ctx.author

            db = await load_money_db()
            moneyDB = db.get("Money", {})
            balance = moneyDB.get(str(member.id), 0)

            embed = discord.Embed(
                title=f"Balance for {member.display_name}:",
                description=f"${format_money(balance)}",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #bal set
    @bal.command()
    async def set(self, ctx, *args):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You do not have permission to use this command.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        member = ctx.author
        amount = None

        if len(args) == 1:
            try:
                amount = float(args[0])
            except ValueError:
                try:
                    member = await commands.MemberConverter().convert(ctx, args[0])
                except commands.MemberNotFound:
                    embed = discord.Embed(
                        title="Member Not Found",
                        color=discord.Color(0x80FF80),
                    )
                    await ctx.reply(embed=embed)
                    return
        elif len(args) >= 2:
            try:
                member = await commands.MemberConverter().convert(ctx, args[0])
            except commands.MemberNotFound:
                embed = discord.Embed(
                    title="Member Not Found",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return
            try:
                amount = float(args[1])
            except ValueError:
                embed = discord.Embed(
                    title="Invalid Amount",
                    description="Amount must be a number.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

        if amount is None:
            embed = discord.Embed(
                title="Usage: #bal set (@user) [=amount]",
                color=discord.Color(0x80FF80),
            )
            embed.set_footer(text="LightslicerGP | #bal set")
            await ctx.reply(embed=embed)
            return

        async with ctx.typing():
            db = await load_money_db()
            moneyDB = db.get("Money", {})
            moneyDB[str(member.id)] = amount
            db["Money"] = moneyDB
            await save_money_db(db)

            display_amount = format_money(amount)

            embed = discord.Embed(
                title="Balance Set",
                description=f"{member.mention}'s balance is now ${display_amount}.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #bal add
    @bal.command()
    async def add(self, ctx, *args):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You do not have permission to use this command.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        member = ctx.author
        amount = None

        if len(args) == 1:
            if args[0].isdigit():
                amount = int(args[0])
            else:
                try:
                    member = await commands.MemberConverter().convert(ctx, args[0])
                except commands.MemberNotFound:
                    mebed = discord.Embed(
                        title="Member Not Found", color=discord.Color(0x80FF80)
                    )
                    await ctx.reply(embed=mebed)
                    return
        elif len(args) >= 2:
            try:
                member = await commands.MemberConverter().convert(ctx, args[0])
            except commands.MemberNotFound:
                embed = discord.Embed(
                    title="Member Not Found",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return
            try:
                amount = int(args[1])
            except ValueError:
                embed = discord.Embed(
                    title="Invalid Amount",
                    description="Amount must be a number.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

        if amount is None:
            embed = discord.Embed(
                title="Usage: #bal add [@user] <amount>",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        if amount < 0:
            embed = discord.Embed(
                title="Invalid Amount",
                description="Amount must be positive.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        async with ctx.typing():
            db = await load_money_db()
            moneyDB = db.get("Money", {})

            current = moneyDB.get(str(member.id), 0)
            if isinstance(current, float):
                moneyDB[str(member.id)] = float(current) + amount
            else:
                moneyDB[str(member.id)] = float(current) + amount

            db["Money"] = moneyDB
            await save_money_db(db)

            embed = discord.Embed(
                title="Balance Added",
                description=f"Added ${format_money(amount)} to {member.mention}'s balance.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #bal remove
    @bal.command()
    async def remove(self, ctx, member: discord.Member, amount: int):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You do not have permission to use this command.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        if amount < 0:
            embed = discord.Embed(
                title="Invalid Amount",
                description="Amount must be positive.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        async with ctx.typing():
            db = await load_money_db()
            moneyDB = db.get("Money", {})
            cur_balance = moneyDB.get(str(member.id), 0)
            new_balance = max(float(cur_balance) - amount, 0.0)
            moneyDB[str(member.id)] = new_balance
            db["Money"] = moneyDB
            await save_money_db(db)

            embed = discord.Embed(
                title="Balance Removed",
                description=f"Removed ${format_money(amount)} from {member.mention}'s balance.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #bal reset
    @bal.command()
    async def reset(self, ctx, *args):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You do not have permission to use this command.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        member = ctx.author

        if args:
            try:
                member = await commands.MemberConverter().convert(ctx, args[0])
            except commands.MemberNotFound:
                embed = discord.Embed(
                    title="Member Not Found",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

        async with ctx.typing():
            db = await load_money_db()
            moneyDB = db.get("Money", {})
            moneyDB[str(member.id)] = 0.0
            db["Money"] = moneyDB
            await save_money_db(db)

            embed = discord.Embed(
                title="Balance Reset",
                description=f"{member.mention}'s balance has been reset to $0.00.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #bal give
    @bal.command()
    async def give(self, ctx, member: discord.Member, amount: int):
        if amount <= 0:
            embed = discord.Embed(
                title="Invalid Amount",
                description="Amount must be positive.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        db = await load_money_db()
        moneyDB = db.get("Money", {})
        sender_id = str(ctx.author.id)
        receiver_id = str(member.id)
        sender_balance = moneyDB.get(sender_id, 0)

        if sender_balance < amount:
            embed = discord.Embed(
                title="Not Enough Balance",
                description="You don't have enough balance to give.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        class ConfirmGive(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=30)
                self.value = None

            @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
            async def yes(
                self, interaction: discord.Interaction, button: discord.ui.Button
            ):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.send_message(
                        "This isn't your confirmation!", ephemeral=True
                    )
                    return
                self.value = True
                self.stop()

            @discord.ui.button(label="No", style=discord.ButtonStyle.red)
            async def no(
                self, interaction: discord.Interaction, button: discord.ui.Button
            ):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.send_message(
                        "This isn't your confirmation!", ephemeral=True
                    )
                    return
                self.value = False
                self.stop()

        async with ctx.typing():
            embed = discord.Embed(
                title="Confirm Transaction",
                description=f"Are you sure you want to give ${format_money(amount)} to {member.mention}?",
                color=discord.Color(0x80FF80),
            )
            view = ConfirmGive()
            message = await ctx.reply(embed=embed, view=view)
            await view.wait()

        if view.value is None:
            await message.edit(
                embed=discord.Embed(
                    title="Transaction Cancelled",
                    description="You did not confirm in time.",
                    color=discord.Color(0x80FF80),
                ),
                view=None,
            )
        elif view.value:
            moneyDB[sender_id] = float(sender_balance) - amount
            moneyDB[receiver_id] = float(moneyDB.get(receiver_id, 0)) + amount
            db["Money"] = moneyDB
            await save_money_db(db)

            await message.edit(
                embed=discord.Embed(
                    title="Balance Given",
                    description=f"{ctx.author.mention} gave ${format_money(amount)} to {member.mention}.",
                    color=discord.Color(0x80FF80),
                ),
                view=None,
            )
        else:
            await message.edit(
                embed=discord.Embed(
                    title="Transaction Cancelled",
                    description="You chose not to give the balance.",
                    color=discord.Color(0x80FF80),
                ),
                view=None,
            )

    # #bal gamble
    @bal.command()
    async def gamble(self, ctx, amount=None):
        async with ctx.typing():
            if amount is None:
                embed = discord.Embed(
                    title="Usage: #bal gamble [amount]",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            try:
                amount = float(amount)
            except (ValueError, TypeError):
                embed = discord.Embed(
                    title="Invalid Amount",
                    description="Amount must be a number.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            if amount <= 0:
                embed = discord.Embed(
                    title="Invalid Amount",
                    description="Amount must be a positive number.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            db = await load_money_db()
            moneyDB = db.get("Money", {})
            user_id = str(ctx.author.id)
            balance = float(moneyDB.get(user_id, 0))

            if balance < amount:
                embed = discord.Embed(
                    title="Not Enough Balance",
                    description="You don't have enough balance to gamble that amount.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            if random.choice([True, False]):
                balance += amount
                result_text = f"You won ${format_money(amount)}!"
            else:
                balance -= amount
                result_text = f"You lost ${format_money(amount)}!"

            moneyDB[user_id] = balance
            db["Money"] = moneyDB
            await save_money_db(db)

            embed = discord.Embed(
                title="Gamble Result",
                description=result_text,
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #gamble
    @commands.command(name="gamble")
    async def gamble_alias(self, ctx, amount=None):
        await self.gamble(ctx, amount)

    # #bal top
    @bal.command()
    async def top(self, ctx):
        async with ctx.typing():
            db = await load_money_db()
            moneyDB = db.get("Money", {})
            sorted_users = sorted(moneyDB.items(), key=lambda x: x[1], reverse=True)[
                :10
            ]

            description = ""
            for i, (user_id, balance) in enumerate(sorted_users, start=1):
                user = ctx.guild.get_member(int(user_id))
                if not user:
                    try:
                        user = await self.bot.fetch_user(int(user_id))
                    except:
                        user = None

                if user:
                    description += (
                        f"{i}. {user.display_name}: ${format_money(balance)}\n"
                    )
                else:
                    description += (
                        f"{i}. Unknown User ({user_id}): ${format_money(balance)}\n"
                    )

            embed = discord.Embed(
                title="Balance Leaderboard",
                description=description or "No data available.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #baltop
    @commands.command(name="baltop")
    async def baltop(self, ctx):
        await self.top(ctx)


async def setup(bot):
    await bot.add_cog(Bal(bot))
