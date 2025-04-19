---
description: Automated bump reminder
---

# #disboard bump

{% hint style="danger" %}
This command is still in development! (aoijs sqlite database issue)
{% endhint %}

## Usage

{% hint style="success" %}
do /bump in your server in the right channel
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // 4/18/25 currently a database issue
  {
    name: "$alwaysExecute",
    code: `
        $setTimeout[DiscordBumpMessage;2h;{"channelID": "$channelID"}]

        $reply[$messageID;true]
        $clientTyping



        $color[#80bfff]
        $description[
            Alright, I will ping the dbump role in 2 hours!
        ]

        $onlyIfMessageContains[$getEmbed[$channelID;$messageID;1;description];DISBOARD: The Public Server List]
        $onlyIf[$channelID==$findNumbers[$getGuildVar[DisboardBumpChannel;$guildID]]]
        $onlyIf[$authorID==302050872383242240]
      `,
  },
  {
    name: "DiscordBumpMessage",
    type: "timeout",
    code: `
        $reply[$messageID;true]



        $channelSendMessage[$timeoutData[channelID];
            Okay <@&972600952655872120>, you can now do discord bump!
        ]
      `,
  },
];
/* 4/18/25 make sure to replace back to this:

      $onlyIfMessageContains[$getEmbed[$channelID;$messageID;1;description];Bump done! :thumbsup:
Check it out [on DISBOARD](https://disboard.org/server/586543238589054997).]

*/
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
print("Hello World!")
```

{% endcode %}
