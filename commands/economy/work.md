---
description: Work for some money
---

# #work

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#work
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // found it was fixed on my birthday 2023! what a nice present :D
  // done 10/5/24
  {
    name: "work",
    code: `
      $clientTyping
      $reply[$messageID;true]



      $color[#80ff80]
      $title[
        You have done some work!
      ]
      $description[Now you have been paid $$numberSeparator[$random[7;121;false]]. Now you have a total of $$numberSeparator[$getGlobalUserVar[Money;$authorID;Bank]] in your balance]



      $setGlobalUserVar[Money;$sum[$getGlobalUserVar[Money;$authorID;Bank];$random[7;121;false]];$authorID;Bank]



      $globalCooldown[60s;
        {newEmbed:
          {title:Slow down!}
          {description:You have to wait %time% before doing the work command again!}
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
