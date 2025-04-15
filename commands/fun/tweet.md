---
description: Make a fake tweet image
---

# #tweet

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#tweet \[text]

* \[text] - required
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  {
    // random ] in the beginning of the send thign
    // fixed 4/14/25 - 4/15/25
    name: "tweet",
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
      $log[https://api.some-random-api.com/canvas/tweet?username=$username[$authorID]&displayname=$userNickname[$guildID;$authorID]&avatar=$replaceText[$authorAvatar;webp;png]&comment=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20]]

      $color[#ffff80]
      $title[
        Here is your tweet $userNickname[$guildID;$authorID]
      ]
      $description[
        Enjoy!
      ]
      $image[
        https://api.some-random-api.com/canvas/tweet?username=$username[$authorID]&displayname=$userNickname[$guildID;$authorID]&avatar=$replaceText[$authorAvatar;webp;png]&comment=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20]
      ]
  
      $onlyIf[$message!=;      
        {newEmbed:
          {title:Please include some text to put in the tweet!}
          {color:#ffff80}
        }
        {reply:$messageID:true}
      ]
    `, //$log[https://some-random-api.ml/canvas/tweet?username=$username[$authorID]&displayname=$username[$authorID]&avatar=$replaceText[$authorAvatar;webp;png]&comment=$replaceText[$message; ;%20]]
  },
];

```
{% endcode %}

{% code title="Discord.py" lineNumbers="true" %}
```python
import discord
from discord.ext import commands
import requests

# 10/1/24 technically done, but api supports custom counts
# and theme, add that as like --theme=dark or whatever idk
# check for parity with the aoijs version 4/5/25


class Tweet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tweet")
    async def command(self, ctx, *, comment=None):
        async with ctx.typing():
            if not comment:
                embed = discord.Embed(
                    title="Please include some text to put in the tweet!",
                    color=discord.Color(0xFFFFFF),
                )
            else:
                user = ctx.author
                username = user.name[:15]
                displayname = user.display_name
                avatar = user.avatar.url
                message = comment.replace(" ", "%20")

                url = f"https://api.some-random-api.com/canvas/tweet?username={username}&displayname={displayname}&avatar={avatar}&comment={message}"
                embed = discord.Embed(
                    title="Here is your tweet",
                    description="Enjoy!",
                    color=discord.Color(0xFFFFFF),
                ).set_image(url=url)

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Tweet(bot))

```
{% endcode %}
