module.exports = [
  {
    //random ] in the beginning of the send thign
    name: "tweet",
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
      $log[https://api.some-random-api.com/canvas/tweet?username=$username[$authorID]&displayname=$userNickname[$guildID;$authorID]&avatar=$replaceText[$authorAvatar;webp;png]&comment=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20]]

      $color[#ffff80]
      $title[
        Here is your tweet $userNickname[$guildID;$authorID]
      ]
      $description[
        Enjoy!
      ]
      $image[
        https://api.some-random-api.com/canvas/tweet?username=$username[$authorID]&displayname=$userNickname[$guildID;$authorID]&avatar=$replaceText[$authorAvatar;webp;png]&comment=$replaceText[$replaceText[$replaceText[$message;&;%26];?;%3F]; ;%20]
      ]
  
      $onlyIf[$message!=;      
        {newEmbed:
          {title:Please include some text to put in the tweet!}
          {color:#ffff80}
        }
        {reply:$messageID:true}
      ]
    `, //$log[https://some-random-api.ml/canvas/tweet?username=$username[$authorID]&displayname=$username[$authorID]&avatar=$replaceText[$authorAvatar;webp;png]&comment=$replaceText[$message; ;%20]]
  },
];
