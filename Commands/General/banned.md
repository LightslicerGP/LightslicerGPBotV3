---
description: Get a list of banned users
---

# #banned

## Usage

{% hint style="success" %}
\#banned
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done yesterday i think 10/5/24
  {
    name: "banned",
    aliases: [`banlist`],
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
  
      $color[#80bfff]
      $title[Banned Users]
      $description[
        $textSplitMap[bannedpeople]
      ]

      $createFile[$usersBanned[$guildID;true;id;\n];banned_ids.txt]
      $textSplit[$usersBanned[$guildID;true;id;§];§]
    `,
  },
  {
    name: "bannedpeople",
    type: "awaited",
    code: `
      $userTag[$message[1]] \`($message[1])\` - $getBanReason[$guildID;$message[1]]
    `,
  },
];

```
{% endcode %}

{% code title="Discord.py" lineNumbers="true" %}
```python
import discord
from discord.ext import commands
import io

# done 10/2/24


class Banlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="banlist")
    async def command(self, ctx):
        async with ctx.typing():

            ban_list = []
            id_list = []

            async for entry in ctx.guild.bans():
                ban_list.append(f"{entry.user} `({entry.user.id})` - {entry.reason}")
                id_list.append(f"{entry.user.id}")

            embed = discord.Embed(
                title="Banned Users",
                description=(
                    "\n".join(ban_list) if ban_list else "No banned users found."
                ),
                color=discord.Color(0x80BFFF),
            )

            file = discord.File(
                io.StringIO("\n".join(id_list)), filename="banned_ids.txt"
            )

        await ctx.reply(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(Banlist(bot))

```
{% endcode %}
