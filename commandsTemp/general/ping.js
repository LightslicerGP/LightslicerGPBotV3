module.exports = [
  // done since like a week ago 10/5/24
  {
    name: "ping",
    code: `
      $clientTyping
      $reply[$messageID;true]


      
      $color[#80bfff]
      $title[
          Pong! 
      ]
      $description[
        Latency: $pingms
      ]
    `,
  },
];
