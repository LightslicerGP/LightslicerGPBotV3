---
description: Get your daily $1,000
---

# #daily

## Usage

{% hint style="success" %}
\#daily
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // when doing this, doing #bal uses the mainsql not banksql, untill you do #baltop or #balset then it fixes????? - shouldve said fixed, 6/8/23, well its 6/9/23 now lol
  // done 10/5/24
  {
    name: "daily",
    code: `
      $clientTyping
      $reply[$messageID;true]



      $setGlobalUserVar[Money;$sum[$getGlobalUserVar[Money;$authorID;Bank];1000];$authorID;Bank]



      $color[#80ff80]
      $title[You have done the daily command!]
      $description[
        Now you have been paid $1,000 and have a total of $$numberSeparator[$sum[$getGlobalUserVar[Money;$authorID;Bank];1000]] in your balance
      ]



      $globalCooldown[24h;
        {newEmbed:
          {title:Slow down!}
            {description:You have to wait %time% before doing the daily command again!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
  `,
  },
];
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
print("Hello World!")
```

{% endcode %}
