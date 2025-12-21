import discord
from discord.ext import commands
import json
import os

with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["token"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="#", intents=intents, help_command=None)

RESTART_STATE_FILE = "restart_state.json"


# @bot.command(name="test")
# async def command(ctx, arg1, arg2="DEFAULT"):
#     async with ctx.typing():
#         content = f"arg1: {arg1}, arg2: {arg2}"
#     await ctx.reply(content)


@bot.command(name="sample")
async def command(ctx, arg1="samplearg"):
    async with ctx.typing():

        embed = discord.Embed(
            title="Sample 1 Text",
            description=arg1,
            color=discord.Color(0xFFFFFF),
        )
        embed.set_image(
            url="https://images.nvidia.com/geforce/news/minecraft-rtx-february-2021-player-worlds-roundup/Kelly-3.jpg"
        )

    await ctx.reply(embed=embed)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    if not os.path.exists(RESTART_STATE_FILE):
        return

    try:
        with open(RESTART_STATE_FILE, "r") as f:
            data = json.load(f)

        channel = bot.get_channel(data["channel_id"])
        if not channel:
            return

        message = await channel.fetch_message(data["message_id"])

        embed = discord.Embed(
            title="Bot Restarted",
            description="The bot has restarted successfully.",
            color=discord.Color(0xFFFFFF),
        )

        await message.edit(embed=embed)

    except Exception as e:
        print("Failed to edit restart message:", e)

    finally:
        os.remove(RESTART_STATE_FILE)


async def load_commands():
    for folder in os.listdir("./commands"):
        folder_path = f"./commands/{folder}"

        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if (
                    file.endswith(".py")
                    and file != "__init__.py"
                    and os.path.getsize(file_path) > 0
                ):
                    ext = f"commands.{folder}.{file[:-3]}"
                    await bot.load_extension(ext)


@bot.event
async def setup_hook():
    await load_commands()


bot.run(TOKEN)
