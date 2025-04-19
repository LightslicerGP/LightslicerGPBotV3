---
description: Give money to another user
---

# #bal give

## Usage

{% hint style="success" %}
\#bal give \[user] \[amount]

- \[user] - required
- \[amount] - required
  {% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // broken
  // WAS broken, past me scammed present me
  // done 10/5/24
  {
    name: "bal give",
    aliases: ["give"],
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $color[#80ff80]
      $title[
        Are you sure you want to send $$numberSeparator[$truncate[$noMentionMessage]] to $username[$mentioned[1]]? Yes/No
      ]
      
      $awaitMessages[$channelID;$authorID;10s;yes,y,no,n;yes,yes,no,no;
        {newEmbed:
          {title:No reply, aborted transaction}
          {color:#80ff80}
        }
        {reply:$messageID:true};
        {
          "amount": "$truncate[$noMentionMessage]",
          "user": "$mentioned[1]"
        }
      ]
    
    
    
      $onlyIf[$noMentionMessage!=0;
        {newEmbed:
          {title:Cannot give $0!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$checkContains[$noMentionMessage;-]==false;
        {newEmbed:
          {title:Cannot give negetive amounts!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$noMentionMessage<=$getGlobalUserVar[Money;$authorID;Bank];
        {newEmbed:
          {title:You do not have that much to give!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$isNumber[$noMentionMessage]==true;
        {newEmbed:
          {title:Input a valid number!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$mentioned[1]!=$authorID;
        {newEmbed:
          {title:You cant give youself money! (this is pointless anyway)}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
    `,
  },
  {
    name: "yes",
    type: "awaited",
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $setGlobalUserVar[Money;$sum[$getGlobalUserVar[Money;$awaitData[user];Bank];$awaitData[amount]];$awaitData[user];Bank]
      $setGlobalUserVar[Money;$sub[$getGlobalUserVar[Money;$authorID;Bank];$awaitData[amount];];$authorID;Bank]
    
    
    
      $color[#80ff80]
      $title[
        Alrighty, you gave $$awaitData[amount] to $userTag[$awaitData[user]]!
      ]
    `,
  },
  {
    name: "no",
    type: "awaited",
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $color[#80ff80]
      $title[
        Alrighty, I aborted the transaction for ya :D
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
