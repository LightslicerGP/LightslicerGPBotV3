---
description: Set the channel for the Bump reminder
---

# #bump channel set

{% hint style="warning" %}
This command is for admins only!
{% endhint %}

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#bump channel set (channel)

* \[channel] - required
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  {
    name: "bump channel set",
    code: `
      $clientTyping
      $reply[$messageID;true]



      $setGuildVar[DisboardBumpChannel;$message;$guildID]
  
      $color[#80bfff]
      $title[Bump Channel has been set!]
      $description[
          Bump channel set to \`$message\`
      ]

      $onlyIf[$guildChannelExists[$guildID;$findChannel[$message;false]]==true;
        {newEmbed:
          {title:Guild does not exist!}
          {color:#80bfff}
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
print("Hello World!")
```
{% endcode %}
