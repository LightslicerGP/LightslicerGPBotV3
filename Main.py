import discord
from discord.ext import commands
import json
import os
import asyncio

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    token = config["token"]
    api_token = config["apiToken"]

intents = discord.Intents.default()
intents.message_content = True
intents.all
bot = commands.Bot(command_prefix="#", intents=intents)


@bot.command(name="test")
async def command(ctx, arg1, arg2="DEFAULT"):
    async with ctx.typing():
        content = f"arg1: {arg1}, arg2: {arg2}"
    await ctx.reply(content)


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
    print(f"Logged in as {bot.user}!")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(
            name=f"On {bot.guilds} servers, and made by LightslicerGP#2125, prefix is #"
        ),
    )


async def load_commands():
    for foldername in os.listdir("./Commands/"):
        if os.path.isdir(f"./Commands/{foldername}"):
            for filename in os.listdir(f"./Commands/{foldername}"):
                if filename.endswith(".py"):
                    await bot.load_extension(f"Commands.{foldername}.{filename[:-3]}")
        elif foldername.endswith(".py"):
            await bot.load_extension(f"Commands.{foldername[:-3]}")


async def main():
    await load_commands()
    await bot.start(token)


asyncio.run(main())
