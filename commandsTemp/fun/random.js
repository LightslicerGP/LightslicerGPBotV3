module.exports = [
  // if doesnt do functions only embeds or som
  {
    name: "random",
    code: `
      $clientTyping
      $reply[$messageID;true]



      $color[#ffff80]
      $title[
          And your number is...
      ]
      $description[
          $get[randomNumber]
      ]
      $footer[
          usage []=optional: #random [lower (default = 0)] [higher (default = 1000)]
      ]

      $let[randomNumber;$random[$get[numberOne];$get[numberTwo]]]

      $let[numberOne;$if[$isNumber[$message[1];$message[1];0]]

      $let[numberTwo;$if[$isNumber[$message[2];$message[2];1000]]
    `,
  },
];
