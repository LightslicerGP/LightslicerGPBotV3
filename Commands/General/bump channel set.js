module.exports = [
  {
    name: "bump channel set",
    code: `
      $clientTyping
      $reply[$messageID;true]



      $setGuildVar[DisboardBumpChannel;$message;$guildID]
  
      $color[#80bfff]
      $title[Bump Channel has been set!]
      $description[
          Bump channel set to \`$message\`
      ]

      $onlyIf[$guildChannelExists[$guildID;$findChannel[$message;false]]==true;
        {newEmbed:
          {title:Guild does not exist!}
          {color:#80bfff}
        }
        {reply:$messageID:true}
      ]
    `,
  },
];
