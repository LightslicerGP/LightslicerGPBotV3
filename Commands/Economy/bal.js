module.exports = [
  // done 10/4/24, ping on reply in parser doesnt work so.....
  // update 10/5/24 6.8.x doesnt ping but 6.9 does, nice
  // update 10/5/24 aoi.db is broken and so doing #bal (user) doesnt get updated after changing database value
  // update 10/5/24 switched to aoi.sqlite, and it works now
  {
    name: "bal",
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $color[#80ff80]
      $title[
        $username[$mentioned[1]] has $$numberSeparator[$truncate[$getGlobalUserVar[Money;$mentioned[1];Bank]]]
      ]
    
    
    
      $globalCooldown[5s;
        {newEmbed:
          {title:Slow down!}
          {description:You have to wait %time% before doing this command again!}
          {color:#80ff80}
        }
        {reply:$messageID:true}
      ]
    `,
  },
];
