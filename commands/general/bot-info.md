---
description: Get information about the bot
---

# #bot info

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#bot info
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // done yesterday/day before, might change idk 10/5/24
  {
    name: "bot info",
    aliases: ["info"],
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
  
      $color[#80bfff]
      $title[Bot Info]
      $description[
          Here is all the inormation you could possibly get from this, enjoy!
      ]
  
  
  
      $image[$userAvatar[$clientID]]
      $addField[Bot Avatar; :arrow_down: Here you go!;true]
      $addField[Node version:;\`$nodeVersion\`;true]
      $addField[Bot RAM Usage;\`$ram\` of \`$maxRam\`;true]
      $addField[Bot CPU Usage;process: \`$cpu[process]\` os: \`$cpu[process]\`;true]
      $addField[Bot Name;$username[$clientID];true]
      $addField[Bot Message Received Ping;\`$messagePing\`;true]
      $addField[Bot er4Database Ping;\`$databasePing\`;true]
      $addField[Bot Ping;\`$pingms\`;true]
      $addField[Bot Uptime;$uptime;true]
      $addField[Commands Count;\`$commandsCount\`;true]
      $addField[Server Count;\`$guildCount\`;true]
      $addField[User Count;\`$allMembersCount\`;true]
      $addField[Bot Creation Date/Time;$creationDate[698733140939898957;date] (yea I know, 3 am lmao);true]
      $addField[Bot Owner;[$username[$clientOwnerIDs]](https://youtube.com/c/LightslicerGP/);true]
    `,
  },
];
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
import discord
from discord.ext import commands
import time

# started 10/3/24, need to add hyperlink to owner and a
# ton of other info still.


class Bot_Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_start_time = time.time()

    @commands.group(name="bot", invoke_without_command=True)
    async def bot(self, ctx):
        async with ctx.typing():
            embed = discord.Embed(
                title="Send a subcommand:",
                description="For now: `#bot info`",
                color=discord.Color(0xFFFFFF),
            )
        await ctx.reply(embed=embed)

    @bot.command(name="info")
    async def info(self, ctx):
        async with ctx.typing():

            app_info = await self.bot.application_info()
            owner = app_info.owner

            creation_time = self.bot.user.created_at.strftime("%m/%d/%Y, %I:%M:%S %p")

            user_count = ctx.guild.member_count

            server_count = len(self.bot.guilds)

            total_commands = len(self.bot.commands)

            uptime = str(round(time.time() - self.bot_start_time))

            ping = round(self.bot.latency)
            message_ping = round(ctx.bot.latency * 1000)

            embed = (
                discord.Embed(
                    title="Bot Info",
                    description="Here is all the inormation you could possibly get from this, enjoy!",
                    color=discord.Color(0x80BFFF),
                )
                .add_field(name="Bot Owner", value=f"{owner}", inline=True)
                .add_field(
                    name="Bot Creation Date/Time", value=creation_time, inline=True
                )
                .add_field(name="User Count", value=f"`{user_count}`", inline=True)
                .add_field(name="Server Count", value=f"`{server_count}`", inline=True)
                .add_field(
                    name="Total Commands", value=f"`{total_commands}`", inline=True
                )
                .add_field(name="Uptime", value=uptime + " seconds", inline=True)
                .add_field(name="Bot Ping", value=f"`{ping}ms`", inline=True)
                .add_field(
                    name="Bot Database Ping",
                    value=f"uhhhh that doesnt exist on py version",
                    inline=True,
                )
                .add_field(
                    name="Bot Message Received Ping",
                    value=f"`{message_ping}ms`",
                    inline=True,
                )
            )

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Bot_Info(bot))

```

{% endcode %}
