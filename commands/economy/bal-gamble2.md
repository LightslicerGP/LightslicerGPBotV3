---
description: gambling 2 electric boogaloo
---

# #bal gamble2

{% hint style="danger" %}
This command is still in development! (and temporary)
{% endhint %}

## Usage

{% hint style="success" %}
\#bal gamble2 \[amount]

- \[amount] - required
  {% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // started 10/6/24, addMessageReactions is broken in 6.8 and 6.9 soooo
  {
    name: "bal gamble2",
    aliases: ["gamble2"],
    code: `
      $clientTyping
      $reply[$messageID;true]

      $awaitComponents[$channelID;$get[messageID];$authorID;btnYes_$message,btnNo;btnYesPressed,btnNoPressed;timeoutError;1;30s]

      $let[messageID;
        $sendMessage[
          {newEmbed:
            {title:Are you sure you want to gamble $$truncate[$message]?}
            {color:#80ff80}
          }
          {reply:$messageID:true}
          {actionRow:
            {button:No:secondary:btnNo:false}
            {button:Yes:danger:btnYes_$message:false}
          };true]
      ]





      $onlyIf[$checkContains[$noMentionMessage;.]==false;
        {newEmbed:
          {title:Cannot gamble decimal amounts!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$noMentionMessage>=1;
        {newEmbed:
          {title:Cannot gamble less than 1!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$checkContains[$noMentionMessage;-]==false;
        {newEmbed:
          {title:Cannot gamble negetive amounts!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$noMentionMessage<=$getGlobalUserVar[Money;$authorID;Bank];
        {newEmbed:
          {title:You do not have that much to gamble!}
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
    `,
  },
  {
    name: "btnYesPressed",
    type: "interaction",
    prototype: "button",
    code: `
      $clientTyping



      $editMessage[$messageID;
        {newEmbed:
          {title:Guess a number!}
          {description:Gambling $$get[gambleAmount]!}
          {color:#80ff80}
        }
        {reply:$messageID:true}

        {actionRow:
          {button:1:secondary:btnOne}
          {button:2:secondary:btnTwo}
          {button:3:secondary:btnThree}
          {button:4:secondary:btnFour}
          {button:5:secondary:btnFive}
        }
        {actionRow:
          {button:6:secondary:btnSix}
          {button:7:secondary:btnSeven}
          {button:8:secondary:btnEight}
          {button:9:secondary:btnNine}
          {button:10:secondary:btnTen}
        }
      ]

      $wait[1s]

      $let[gambleAmount;$splitText[2]]
      $textSplit[$interactionData[customId];_]
    `,
  },

  {
    name: "btnNoPressed",
    type: "interaction",
    prototype: "button",
    code: `
      $clientTyping

      $editMessage[$messageID;
        {newEmbed:
          {title:Alrighty, gambling addiction has been stopped!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
    `,
  },
  ,
  {
    name: "timeoutError",
    type: "awaited",
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $color[#80ff80]
      $title[
        Alrighty, gambling addiction has been stopped!
      ]
    `,
  },
  {
    name: "btnOne",
    type: "interaction",
    prototype: "button",
    $if: "old",
    code: `
      $clientTyping


      $editMessage[$messageID;

        $if[$random[1;10;false;false]==1]

          {newEmbed:
            {title:WIN $random[1;10;false;false]}
            {color:#80ff80}
          }
          {reply:$messageID:true}

        $else

          {newEmbed:
            {title:FAIL $random[1;10;false;false]}
            {color:#80ff80}
          }
          {reply:$messageID:true}
          
        $endif
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
