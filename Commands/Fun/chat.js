module.exports = [
  // 9/30/24 doing anything but hi or hello doesnt work lol, api is broken
  // (calling it) done (ig) 10/5/24
  // 4/14/25 they updated the api, fixed all api stuff now lmao
  {
    name: "chat",
    code: `
      $clientTyping
      $reply[$messageID;true]


      $log[https://api.some-random-api.com/chatbot?key=$getObjectProperty[apiToken;apiToken]&message=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20]]

      $color[#ffff80]
      $title[
          LightslicerGPBot responds:
      ]
      $description[
          $jsonRequest[https://api.some-random-api.com/chatbot?key=$getObjectProperty[apiToken;apiToken]&message=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20];response;false response given, sad]
      ]
      $createObject[apiToken;$readFile[./config.json]]



      $onlyIf[$message!=;
          {newEmbed:
            {title:Please include some text for the bot to reply to!!}
            {color:#ffff80}
          }
          $reply[$messageID;true]
      ]
    `,
  },
];
