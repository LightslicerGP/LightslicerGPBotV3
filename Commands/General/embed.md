---
description: Embed template command
---

# #embed

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#embed
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
console.log("Hello World!")
```
{% endcode %}

{% code title="Discord.py" lineNumbers="true" %}
```python
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
                    url="https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-caves-and-cliffs-supprt-as-well-as-discord_5.png",
                    icon_url="https://api.mcpedl.com/storage/submissions/99076/images/kellys-minecraft-vanilla-rtx-conversion-pack-massive-update_4.jpeg",
                )
                .set_footer(
                    text="FooterTextGoesHere",
                    icon_url="https://lightslicergp.netlify.app",
                )
                .set_thumbnail(
                    url="https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-clear-water-and-another-addon_8.png"
                )
                .set_image(
                    url="https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-caves-and-cliffs-supprt-as-well-as-discord_5.png"
                )
                .add_field(
                    name="AddFieldTextGoesHere",
                    value="AddFieldValueGoesHere",
                    inline=False,
                )
                .add_field(
                    name="AddFieldTextGoesHere",
                    value="AddFieldValueGoesHere",
                    inline=False,
                )
                .add_field(
                    name="AddFieldTextGoesHere",
                    value="AddFieldValueGoesHere",
                    inline=False,
                )
            )

            view = View()

            button_primary = Button(
                label="Primary", style=discord.ButtonStyle.primary, row=1
            )
            button_secondary = Button(
                label="Secondary", style=discord.ButtonStyle.secondary, row=1
            )
            button_success = Button(
                label="Success", style=discord.ButtonStyle.success, row=1
            )
            button_danger = Button(
                label="Danger", style=discord.ButtonStyle.danger, row=1
            )
            button_link = Button(
                label="Link",
                style=discord.ButtonStyle.link,
                url="https://example.com",
                row=1,
            )

            button_primary_disabled = Button(
                label="Primary Disabled",
                style=discord.ButtonStyle.primary,
                disabled=True,
                row=2,
            )
            button_secondary_disabled = Button(
                label="Secondary Disabled",
                style=discord.ButtonStyle.secondary,
                disabled=True,
                row=2,
            )
            button_success_disabled = Button(
                label="Success Disabled",
                style=discord.ButtonStyle.success,
                disabled=True,
                row=2,
            )
            button_danger_disabled = Button(
                label="Danger Disabled",
                style=discord.ButtonStyle.danger,
                disabled=True,
                row=2,
            )
            button_link_disabled = Button(
                label="Link Disabled",
                style=discord.ButtonStyle.link,
                url="https://example.com",
                disabled=True,
                row=2,
            )

            view.add_item(button_primary)
            view.add_item(button_secondary)
            view.add_item(button_success)
            view.add_item(button_danger)
            view.add_item(button_link)

            view.add_item(button_primary_disabled)
            view.add_item(button_secondary_disabled)
            view.add_item(button_success_disabled)
            view.add_item(button_danger_disabled)
            view.add_item(button_link_disabled)

        await ctx.reply(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Embed(bot))

```
{% endcode %}
