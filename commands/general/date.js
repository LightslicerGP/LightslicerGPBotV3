module.exports = [
  // Done 4/18/25
  {
    name: "date",
    code: `
        $clientTyping
        $reply[$messageID;true]



        $color[#80bfff]
        $title[
            Here is the date and time in Eastern Daylight Time (EDT)
        ]
        $description[
            $parseDate[$math[$dateStamp-14400000];date]
        ]
        $footer[
            this is in MM/DD/YYYY, H:MM:SS XX format
        ]
        `,
  },
];
