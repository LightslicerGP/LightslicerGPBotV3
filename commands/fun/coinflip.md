---
description: Flip a coin
---

# #coinflip

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#coinflip
{% endhint %}

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
console.log("Hello World!")
```
{% endcode %}

{% code title="Discord.py" lineNumbers="true" %}
```python
import discord
from discord.ext import commands
import random

# done 10/1/24


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coinflip", aliases=["flip"])
    async def command(self, ctx):
        async with ctx.typing():

            result = random.randint(1, 1001)
            if result == 1:
                description = "***The coin somehow landed on its edge i dont know how i dont make the rules and i cant manipulate an RNG for it to do so but somehow you managed a 1/1001 chance of getting this, feel proud!***"
            elif result <= 501:
                description = "Heads"
            else:
                description = "Tails"

            embed = discord.Embed(
                title="And you flipped...",
                description=description,
                color=discord.Color(0xFFFF80),
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Coinflip(bot))

```
{% endcode %}
