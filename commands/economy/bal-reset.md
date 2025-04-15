---
description: Reset a user's balance
---

# #bal reset

{% hint style="warning" %}
This command is for admins only!
{% endhint %}

## Usage

{% hint style="success" %}
\#bal reset (user) \[amount]

* (user) - optional
* \[amount] - required
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done 10/5/24
  {
    name: "bal reset",
    aliases: ["balreset"],
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $setGlobalUserVar[Money;;$mentioned[1];Bank]
    
    
    
      $color[#80ff80]
      $title[
        You have reset $username[$mentioned[1]]'s money
      ]
      $description[
        $username[$mentioned[1]] orignally had $$numberSeparator[$getGlobalUserVar[Money;$mentioned[1];Bank]] 
      ]
    
    
    
      $onlyForIDs[586225258269245538;883931596758081556;
        {newEmbed:
          {title:You're not LightslicerGP (nor an admin), and I (the bot) can't make you him sooo..... sorry I guess}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$mentionedUsersCount<=1;
        {newEmbed:
          {title:Only mention one person!}
          {color:#80ff80}
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
