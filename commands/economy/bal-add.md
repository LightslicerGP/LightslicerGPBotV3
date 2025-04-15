---
description: Add to a user's balance
---

# #bal add

## Usage

{% hint style="warning" %}
This command is for admins only!
{% endhint %}

{% hint style="success" %}
\#bal add \[user] \[amount]

* \[user] - required
* \[amount] - required
{% endhint %}

{% code lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // new from 10/5/24, done same day
  // note: can use negative numbers for #bal remove ig lol
  {
    name: "bal add",
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $setGlobalUserVar[Money;$sum[$getGlobalUserVar[Money;$mentioned[1];Bank];$noMentionMessage];$mentioned[1];Bank]
    
    
    
      $color[#80ff80]
      $title[
        You have added $$noMentionMessage to $username[$mentioned[1]]'s money
      ]
      $description[
        $username[$mentioned[1]] now has $$math[$getGlobalUserVar[Money;$mentioned[1];Bank]+$noMentionMessage]
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
