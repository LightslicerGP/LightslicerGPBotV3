---
description: Get a random number
---

# #random

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#random (minimum) (maximum)

- (minimum) - optional
- (maximum) - optional
  {% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // if doesnt do functions only embeds or som
  {
    name: "random",
    code: `
      $clientTyping
      $reply[$messageID;true]



      $color[#ffff80]
      $title[
          And your number is...
      ]
      $description[
          $get[randomNumber]
      ]
      $footer[
          usage []=optional: #random [lower (default = 0)] [higher (default = 1000)]
      ]

      $let[randomNumber;$random[$get[numberOne];$get[numberTwo]]]

      $let[numberOne;$if[$isNumber[$message[1];$message[1];0]]

      $let[numberTwo;$if[$isNumber[$message[2];$message[2];1000]]
    `,
  },
];
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
import discord
from discord.ext import commands
import random

# done 10/1/24


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="random")
    async def command(self, ctx, arg1=0, arg2=1000):
        async with ctx.typing():

            embed = discord.Embed(
                title="And your number is...",
                description=str(random.randint(int(arg1), int(arg2))),
                color=discord.Color(0xFFFFFF),
            ).set_footer(
                text="usage []=optional: #random [lower (default = 0)] [higher (default = 1000)]"
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Random(bot))

```

{% endcode %}
