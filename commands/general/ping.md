---
description: Get the ping to the bot
---

# #ping

## Usage

{% hint style="success" %}
\#ping
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // done since like a week ago 10/5/24
  {
    name: "ping",
    code: `
      $clientTyping
      $reply[$messageID;true]


      
      $color[#80bfff]
      $title[
          Pong! 
      ]
      $description[
        Latency: $pingms
      ]
    `,
  },
];
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
import discord
from discord.ext import commands

# done 10/1/24


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def command(self, ctx):
        async with ctx.typing():

            latency = round(self.bot.latency * 1000)

            embed = discord.Embed(
                title="Pong!",
                description=f"Latency: {latency}ms",
                color=discord.Color(0x80BFFF),
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Ping(bot))

```

{% endcode %}
