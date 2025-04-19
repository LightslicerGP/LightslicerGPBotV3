import discord
from discord.ext import commands
from discord.ui import Button, View

# mabye cleanup idk 10/1/24, done


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed")
    async def command(self, ctx):
        async with ctx.typing():

            embed = (
                discord.Embed(
                    title="TitleTextGoesHere",
                    description="DescriptionTextGoesHere",
                    color=discord.Color(0x80BFFF),
                    timestamp=ctx.message.created_at,
                )
                .set_author(
                    name="AuthorTextGoesHere",
                    url="https://lightslicergp.gitbook.io/lightslicergpbotv3/",
                    icon_url="https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-caves-and-cliffs-supprt-as-well-as-discord_5.png",
                )
                .set_footer(
                    text="FooterTextGoesHere",
                    icon_url="https://lightslicergp.netlify.app",
                )
                .set_thumbnail(
                    url="https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-clear-water-and-another-addon_8.png"
                )
                .set_image(
                    url="https://images.nvidia.com/geforce/news/minecraft-rtx-february-2021-player-worlds-roundup/Kelly-3.jpg"
                )
                .add_field(
                    name="AddFieldTextGoesHere",
                    value="AddFieldValueGoesHere",
                    inline=True,
                )
                .add_field(
                    name="AddFieldTextGoesHere",
                    value="AddFieldValueGoesHere",
                    inline=True,
                )
                .add_field(
                    name="AddFieldTextGoesHere",
                    value="AddFieldValueGoesHere",
                    inline=True,
                )
            )

            view = View()

            button_primary = Button(
                label="label", style=discord.ButtonStyle.primary, row=1
            )
            button_secondary = Button(
                label="label", style=discord.ButtonStyle.secondary, row=1
            )
            button_success = Button(
                label="label", style=discord.ButtonStyle.success, row=1
            )
            button_danger = Button(
                label="label", style=discord.ButtonStyle.danger, row=1
            )
            button_link = Button(
                label="label",
                style=discord.ButtonStyle.link,
                url="https://lightslicergp.gitbook.io/lightslicergpbotv3/",
                row=1,
            )

            button_primary_disabled = Button(
                label="label",
                style=discord.ButtonStyle.primary,
                disabled=True,
                row=2,
            )
            button_secondary_disabled = Button(
                label="label",
                style=discord.ButtonStyle.secondary,
                disabled=True,
                row=2,
            )
            button_success_disabled = Button(
                label="label",
                style=discord.ButtonStyle.success,
                disabled=True,
                row=2,
            )
            button_danger_disabled = Button(
                label="label",
                style=discord.ButtonStyle.danger,
                disabled=True,
                row=2,
            )
            button_link_disabled = Button(
                label="label",
                style=discord.ButtonStyle.link,
                url="https://lightslicergp.gitbook.io/lightslicergpbotv3/",
                disabled=True,
                row=2,
            )

            view.add_item(button_link)
            view.add_item(button_danger)
            view.add_item(button_success)
            view.add_item(button_secondary)
            view.add_item(button_primary)

            view.add_item(button_link_disabled)
            view.add_item(button_danger_disabled)
            view.add_item(button_success_disabled)
            view.add_item(button_secondary_disabled)
            view.add_item(button_primary_disabled)

        await ctx.reply(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Embed(bot))
