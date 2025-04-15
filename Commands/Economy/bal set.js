module.exports = [
  // done 10/4/24, ping on reply in parser doesnt work so.....
  // update 10/5/24 6.8.x doesnt ping but 6.9 does, nice
  {
    name: "bal set",
    aliases: ["setbal"],
    code: `
      $clientTyping
      $reply[$messageID;true]
      
      $setGlobalUserVar[Money;$truncate[$noMentionMessage];$mentioned[1];Bank]
    
    
    
      $color[#80ff80]
      $title[
        You have set a user's balance!
      ]
      $description[
        The user $username[$mentioned[1]] now has $$numberSeparator[$truncate[$noMentionMessage]]
      ]
    
    
    
      $onlyForIDs[586225258269245538;883931596758081556;
        {newEmbed:
          {title:You're not LightslicerGP (nor an admin), and I (the bot) can't make you him sooo..... sorry I guess}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
      $onlyIf[$isNumber[$noMentionMessage]==true;
        {newEmbed:
          {title:Input a valid amount!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
    `,
  },
];
