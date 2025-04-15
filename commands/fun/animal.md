---
description: Get a random info card for an animal!
---

# #animal

## Usage

{% hint style="success" %}
\#command \[animal]

* \[animal] - required
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done 9/30/24
  {
    name: "animal",
    aliases: ["animals"],
    code: `
        $clientTyping
        $reply[$messageID;true]



        $color[#ffff80]
        $title[
List of animals you can do:
- Dog
- Cat
- Bird
- Fox
- Koala
- Panda
- Kangaroo
- Raccoon

        ]
        $description[
            Enjoy!
        ]
    `,
  },
  {
    name: "animal dog",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your dog picture and fact!
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/dog;fact;rip theres no dog fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/dog;image;rip theres no dog picture]
    ]
    `,
  },
  {
    name: "animal cat",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your cat picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/cat;fact;rip theres no cat fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/cat;image;rip theres no cat picture]
    ]
    `,
  },
  {
    name: "animal bird",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your bird picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/bird;fact;rip theres no bird fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/bird;image;rip theres no bird picture]
    ]
    `,
  },
  {
    name: "animal fox",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your fox picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/fox;fact;rip theres no fox fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/fox;image;rip theres no fox picture]
    ]
    `,
  },
  {
    name: "animal koala",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your koala picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/koala;fact;rip theres no koala fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/koala;image;rip theres no koala picture]
    ]
    `,
  },
  {
    name: "animal panda",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your panda picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/panda;fact;rip theres no panda fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/panda;image;rip theres no panda picture]
    ]
    `,
  },
  {
    name: "animal kangaroo",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your kangaroo picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/kangaroo;fact;rip theres no kangaroo fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/kangaroo;image;rip theres no kangaroo picture]
    ]
    `,
  },
  {
    name: "animal raccoon",
    code: `
    $clientTyping
    $reply[$messageID;true]



    $color[#ffff80]
    $title[
        Here is your raccoon picture
    ]
    $description[
        $jsonRequest[https://api.some-random-api.com/animal/raccoon;fact;rip theres no raccoon fact]
    ]
    $image[
        $jsonRequest[https://api.some-random-api.com/animal/raccoon;image;rip theres no raccoon picture]
    ]
    `,
  },
];

```
{% endcode %}

{% hint style="danger" %}
This command is still in development!
{% endhint %}

{% code title="Discord.py" lineNumbers="true" %}
```python
import discord
from discord.ext import commands
import requests

# done 9/30/24


class Animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="animal")
    async def command(self, ctx, animal="None"):
        async with ctx.typing():
            if animal.lower() in ["dog", "cat", "bird", "fox", "koala", "panda"]:
                animal = animal.lower()
                response = requests.get(
                    f"https://api.some-random-api.com/animal/{animal}"
                ).json()
                embed = discord.Embed(
                    title=f"Here is your {animal} picture and fact!",
                    description=response.get("fact", f"rip theres no {animal} fact"),
                    color=discord.Color(0xFFFF80),
                )
                embed.set_image(
                    url=response.get("image", f"rip theres no {animal} picture")
                )
            else:
                embed = discord.Embed(
                    title="List of animals you can do:\n- Dog\n- Cat\n- Bird\n- Fox\n- Koala\n- Panda",
                    description="Enjoy!",
                    color=discord.Color(0xFFFF80),
                )
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Animal(bot))

```
{% endcode %}
