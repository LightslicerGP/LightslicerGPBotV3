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
