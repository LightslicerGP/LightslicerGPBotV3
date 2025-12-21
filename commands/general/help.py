import discord
from discord.ext import commands
from discord.ui import View
from discord.ui.select import Select

# done but pls update when a new command is done/added 12/17/25

CATEGORY_META = {
    "Economy": {
        "color": 0x80FF80,
        "emoji": "💵",
        "description": "All money and economy related commands",
        "commands": [
            {
                "name": "bal `(@user)`",
                "subcommands": [
                    r"\*add `(@user) [=amount]`",
                    "gamble `[=amount]`",
                    "give `[@user] [=amount]`",
                    r"\*remove `[@user] [=amount]`",
                    r"\*reset `[@user]`",
                    r"\*set `(@user) [=amount]`",
                    "top",
                ],
            },
            {"name": "daily"},
            {
                "name": "job `(@user)`",
                "subcommands": [
                    "apply `[>job|=jobNumber]`",
                    r"\*give `(@user) [>job|=jobNumber]`",
                    r"\*raise reset `(@user) [>job|=jobNumber] [=amount]`",
                    r"\*raise set `(@user) [>job|=jobNumber]`",
                    r"\*remove `(@user) [>job|=jobNumber]`",
                ],
            },
            {
                "name": "shop",
                "subcommands": [
                    "shop buy `[>item]`",
                ],
            },
            {"name": "work"},
        ],
    },
    "Fun": {
        "color": 0xFFFF80,
        "emoji": "🎮",
        "description": "All fun and random commands that some of which use some-random-api.com!",
        "commands": [
            {"name": "animal `[>animal]`"},
            {"name": "chat `[.message]`"},
            {"name": "comment `[.message]`"},
            {"name": "coinflip"},
            {"name": "diceroll"},
            {"name": "random `(=min:1) (=max:100)`"},
            {"name": "tweet `[.message]`"},
        ],
    },
    "General": {
        "color": 0x80BFFF,
        "emoji": "⚙️",
        "description": "General commands that give information or edit settings",
        "commands": [
            {"name": "banned `(@user)`", "aliases": ["banlist"]},
            {"name": "bot info"},
            {"name": r"\*bot restart"},
            {
                "name": "bump",
                "subcommands": [
                    # "bump ping",
                    "bump channel set `(#channel:current)`",
                    "bump channel",
                    "bump role set `[@role]`",
                    "bump role",
                ],
            },
            # {"name": "calc `[.equation]`"},
            # {"name": "date"},
            # {"name": "embed"},
            # {"name": "eval `[.code]`"},
            {"name": "test"},
            # {"name": "help `[>command]`"},
            # {"name": "invite"},
            {"name": "ping"},
            # {"name": "rawjson `[.json]`"},
            # {"name": "version"},
            # {"name": "whois `[@user]`"},
        ],
    },
    "Profile": {
        "color": 0xFF8080,
        "emoji": "👤",
        "description": "All personal profiles with their information",
        "commands": [
            {
                "name": "profile `(@user)`",
                "subcommands": [
                    "set `[bio|birthday|color|interests|youtube|site] [.text]`",
                ],
            }
        ],
    },
    # "Pet": {
    #     "color": 0xFFC080,
    #     "emoji": "🐾",
    #     "description": "PETSSSSSSSSSSSSSSSSSSSSSSSS",
    # },
}

DEFAULT_META = {
    "color": 0x2F3136,
    "emoji": "📁",
    "description": "Miscellaneous commands",
    "commands": [],
}

# next
# 0xc080ff
# 0xff80c0


def get_categories():
    return list(CATEGORY_META.keys())


def get_category_meta(category: str):
    return CATEGORY_META.get(category, DEFAULT_META)


def find_command_in_meta(name: str):
    name = name.lower()

    for category, meta in CATEGORY_META.items():
        for cmd in meta.get("commands", []):
            if cmd["name"] == name:
                return category, cmd

            if name in cmd.get("aliases", []):
                return category, cmd

            if name in cmd.get("subcommands", []):
                return category, cmd

    return None, None


class CategorySelect(Select):
    def __init__(self, view):
        options = []

        for i, category in enumerate(view.categories):
            meta = get_category_meta(category)
            options.append(
                discord.SelectOption(
                    label=category,
                    emoji=meta["emoji"],
                    description=meta["description"],
                    value=str(i),
                )
            )

        super().__init__(
            placeholder="Select a command category…",
            min_values=1,
            max_values=1,
            options=options,
        )

        self.view_ref = view

    async def callback(self, interaction: discord.Interaction):
        self.view_ref.index = int(self.values[0])
        await interaction.response.edit_message(
            embed=self.view_ref.get_embed(),
            view=self.view_ref,
        )


class HelpView(View):
    def __init__(self):
        super().__init__(timeout=120)
        self.categories = get_categories()
        self.index = 0
        self.add_item(CategorySelect(self))

    def get_embed(self):
        category = self.categories[self.index]
        meta = get_category_meta(category)

        embed = discord.Embed(
            title=f"{meta['emoji']} {category} Commands",
            description=meta["description"],
            color=discord.Color(meta["color"]),
        )

        commands = meta.get("commands", [])

        if not commands:
            embed.add_field(
                name="No Commands",
                value="No commands configured for this category.",
                inline=False,
            )
            return embed

        lines = []

        for cmd in commands:
            line = f"{cmd['name']}"

            if "aliases" in cmd:
                aliases = ", ".join(f"{a}" for a in cmd["aliases"])
                line += f" (aliases: {aliases})"

            if "subcommands" in cmd:
                # Each subcommand gets its own line with the arrow
                sub_lines = []
                for s in cmd["subcommands"]:
                    sub_lines.append(f"↳{s}")
                line += "\n" + "\n".join(sub_lines)

            lines.append(line)

        embed.add_field(
            name="Commands",
            value="\n".join(lines),
            inline=False,
        )

        embed.set_footer(
            text="[] = required\n() = optional\n\n @ = user/role\n # = channel\n = = number\n > = listed option\n . = string\n : = default option\n | = logical OR\n * = user <@586225258269245538> only"
        )

        return embed


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx, *, command_name: str = None):
        if command_name:
            category, cmd = find_command_in_meta(command_name)

            if not cmd:
                await ctx.reply("Command not found.")
                return

            meta = get_category_meta(category)

            embed = discord.Embed(
                title=f"{meta['emoji']} Help: {cmd['name']}",
                color=discord.Color(meta["color"]),
            )

            if "aliases" in cmd:
                embed.add_field(
                    name="Aliases",
                    value=", ".join(f"`{a}`" for a in cmd["aliases"]),
                    inline=False,
                )

            if "subcommands" in cmd:
                embed.add_field(
                    name="Subcommands",
                    value=", ".join(f"`{cmd['name']} {s}`" for s in cmd["subcommands"]),
                    inline=False,
                )

            embed.add_field(
                name="Category",
                value=category,
                inline=False,
            )

            await ctx.reply(embed=embed)
            return

        view = HelpView()
        await ctx.reply(embed=view.get_embed(), view=view)


async def setup(bot):
    await bot.add_cog(Help(bot))
