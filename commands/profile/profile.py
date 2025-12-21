import discord
from discord.ext import commands
import json
import os

# done 12/17/25

DB_FILE = "database.json"


def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="profile")
    async def profile(self, ctx, *, arg: str = None):
        db = load_db()
        profiles = db.setdefault("Profile", {})

        # ───────────────
        # SHOW PROFILE
        # ───────────────
        if not arg or arg.startswith("<@"):
            user = ctx.message.mentions[0] if ctx.message.mentions else ctx.author

            user_id = str(user.id)
            profile = profiles.get(user_id)

            if not profile:
                await ctx.reply("This user does not have a profile yet.")
                return

            embed = discord.Embed(
                title=f"👤 {user.display_name}'s Profile",
                color=discord.Color(0xFF8080),
            )
            embed.set_thumbnail(url=user.display_avatar.url)

            for key, value in profile.items():
                field_name = key.replace("_", " ")

                # Handle nested objects (like Birthday)
                if isinstance(value, dict):
                    formatted = []
                    for k, v in value.items():
                        if v is not None:
                            formatted.append(f"{k}: {v}")
                    field_value = "\n".join(formatted) or "Not set"
                else:
                    field_value = str(value)

                embed.add_field(
                    name=field_name,
                    value=field_value,
                    inline=False,
                )

            await ctx.reply(embed=embed)
            return

        # ───────────────
        # SET PROFILE
        # ───────────────
        parts = arg.split(maxsplit=2)

        if parts[0].lower() != "set" or len(parts) < 3:
            await ctx.reply(
                "Invalid usage.\n"
                "**Examples:**\n"
                "`#profile`\n"
                "`#profile @user`\n"
                "`#profile set bio Hello world`"
            )
            return

        field = parts[1].capitalize()
        value = parts[2]

        user_id = str(ctx.author.id)
        user_profile = profiles.setdefault(user_id, {})

        # Special handling for birthday
        if field.lower() == "birthday":
            pieces = value.split()
            if len(pieces) < 2:
                await ctx.reply("Birthday format: `Month Day [Year]`")
                return

            user_profile["Birthday"] = {
                "Month": pieces[0],
                "Day": int(pieces[1]),
                "Year": int(pieces[2]) if len(pieces) > 2 else None,
            }
        else:
            user_profile[field] = value

        save_db(db)

        await ctx.reply(f"Updated **{field}** in your profile.")


async def setup(bot):
    await bot.add_cog(Profile(bot))
