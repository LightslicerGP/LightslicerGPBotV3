---
description: View a user's balance
---

# #bal

## Usage

{% hint style="success" %}
\#bal (user)

* (user) - optional
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done 10/4/24, ping on reply in parser doesnt work so.....
  // update 10/5/24 6.8.x doesnt ping but 6.9 does, nice
  // update 10/5/24 aoi.db is broken and so doing #bal (user) doesnt get updated after changing database value
  // update 10/5/24 switched to aoi.sqlite, and it works now
  {
    name: "bal",
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $color[#80ff80]
      $title[
        $username[$mentioned[1]] has $$numberSeparator[$truncate[$getGlobalUserVar[Money;$mentioned[1];Bank]]]
      ]
    
    
    
      $globalCooldown[5s;
        {newEmbed:
          {title:Slow down!}
          {description:You have to wait %time% before doing this command again!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
    `,
  },
];

```
{% endcode %}

{% code title="Discord.py" lineNumbers="true" %}
```python
import discord
from discord.ext import commands
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    token = config["token"]
    api_token = config["apiToken"]

# TO DO

class Bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Bal")
    async def command(self, ctx, arg1="sample2arg"):
        async with ctx.typing():

            embed = discord.Embed(
                title="{} has ${}",
                description=arg1,
                color=discord.Color(0x80FF80),
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Bal(bot))

```
{% endcode %}
