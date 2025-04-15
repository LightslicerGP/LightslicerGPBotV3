---
description: Gamble your life savings away, forget the college fund :D
---

# #bal gamble

{% hint style="danger" %}
This command is still in development! (probably for a while too, its complicated)
{% endhint %}

## Usage

{% hint style="success" %}
\#bal gamble \[amount]

* \[amount] - required
{% endhint %}

## Code

{% code title="Main" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // just for stickman :)
  {
    name: "bal gamble",
    aliases: ["gamble"],
    code: `
        $clientTyping
        $reply[$messageID;true]
    
        $ifAwaited[$random[1;3;false;false]==2;{execute:won};{execute:lost}]
        $createTemporaryVar[main;gambleNum:$random[1;3;false;false]]

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
    name: "won",
    type: "awaited",
    code: `
        $clientTyping
        $reply[$messageID;true]

        you WONNNNNNNNN $$math[2*$message] YAYAYAYYAYY (you now have $$truncate[$getGlobalUserVar[Money;$authorID;Bank]]) (the number was $getVar[gambleNum;main])
        $setGlobalUserVar[Money;$math[$getGlobalUserVar[Money;$authorID;Bank]+(2*$message)];$authorID;Bank]
    `,
  },
  {
    name: "lost",
    type: "awaited",
    code: `
        $clientTyping
        $reply[$messageID;true]

        you lost boo hooo, HAHA GET GOOD (you now have $$truncate[$getGlobalUserVar[Money;$authorID;Bank]])  (the number was $getVar[gambleNum;main])
        $setGlobalUserVar[Money;$sub[$getGlobalUserVar[Money;$authorID;Bank];$message];$authorID;Bank]
    `,
  },
];

```
{% endcode %}

{% code title="Second, to do." lineNumbers="true" %}
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
