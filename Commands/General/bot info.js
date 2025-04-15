module.exports = [
  // done yesterday/day before, might change idk 10/5/24
  {
    name: "bot info",
    aliases: ["info"],
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
  
      $color[#80bfff]
      $title[Bot Info]
      $description[
          Here is all the inormation you could possibly get from this, enjoy!
      ]
  
  
  
      $image[$userAvatar[$clientID]]
      $addField[Bot Avatar; :arrow_down: Here you go!;true]
      $addField[Node version:;\`$nodeVersion\`;true]
      $addField[Bot RAM Usage;\`$ram\` of \`$maxRam\`;true]
      $addField[Bot CPU Usage;process: \`$cpu[process]\` os: \`$cpu[process]\`;true]
      $addField[Bot Name;$username[$clientID];true]
      $addField[Bot Message Received Ping;\`$messagePing\`;true]
      $addField[Bot er4Database Ping;\`$databasePing\`;true]
      $addField[Bot Ping;\`$pingms\`;true]
      $addField[Bot Uptime;$uptime;true]
      $addField[Commands Count;\`$commandsCount\`;true]
      $addField[Server Count;\`$guildCount\`;true]
      $addField[User Count;\`$allMembersCount\`;true]
      $addField[Bot Creation Date/Time;$creationDate[698733140939898957;date] (yea I know, 3 am lmao);true]
      $addField[Bot Owner;[$username[$clientOwnerIDs]](https://youtube.com/c/LightslicerGP/);true]
    `,
  },
];
