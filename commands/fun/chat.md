---
description: Talk to an ai bot
---

# #chat

## Usage

{% hint style="success" %}
\#chat \[text]

- \[text] - required
  {% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // 9/30/24 doing anything but hi or hello doesnt work lol, api is broken
  // (calling it) done (ig) 10/5/24
  // 4/14/25 they updated the api, fixed all api stuff now lmao
  {
    name: "chat",
    code: `
      $clientTyping
      $reply[$messageID;true]


      $log[https://api.some-random-api.com/chatbot?key=$getObjectProperty[apiToken;apiToken]&message=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20]]

      $color[#ffff80]
      $title[
          LightslicerGPBot responds:
      ]
      $description[
          $jsonRequest[https://api.some-random-api.com/chatbot?key=$getObjectProperty[apiToken;apiToken]&message=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20];response;false response given, sad]
      ]
      $createObject[apiToken;$readFile[./config.json]]



      $onlyIf[$message!=;
          {newEmbed:
            {title:Please include some text for the bot to reply to!!}
            {color:#ffff80}
          }
          $reply[$messageID;true]
      ]
    `,
  },
];
```

{% endcode %}

{% hint style="danger" %}
This command is still in development!
{% endhint %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
import discord
from discord.ext import commands
import requests

# done 10/1/24
# to do, check if it works 4/15/25

api_token = 0


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chat")
    async def command(self, ctx, arg1="sample2arg"):
        async with ctx.typing():

            if arg1:
                message = arg1.replace(" ", "%20")
                response = requests.get(
                    f"https://api.some-random-api.com/chatbot?key={api_token}&message={message}"
                ).json()
                embed = discord.Embed(
                    title="LightslicerGPBot responds:",
                    description=response.get("response", "false response given, sad"),
                    color=discord.Color(0xFFFF80),
                )
            else:
                embed = discord.Embed(
                    title="Please include some text for the bot to reply to!!",
                    color=discord.Color(0xFFFF80),
                )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Chat(bot))

```

{% endcode %}
