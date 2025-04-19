module.exports = [
    // 4/18/25 based on the discord.py version, $author (and others) should have support for hyperlinks
    {
      name: "embed",
      code: `
        $clientTyping
        $reply[$messageID;true]
    
    
    
        $color[#80bfff]
        $title[TitleTextGoesHere]
        $description[DescriptionTextGoesHere]
        $footer[FooterTextGoesHere;https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-clear-water-and-another-addon_3.png]
        $addTimestamp[$datestamp]
        $addField[AddFieldTextGoesHere;AddFieldValueGoesHere;true]
        $addField[AddFieldTextGoesHere;AddFieldValueGoesHere;true]
        $addField[AddFieldTextGoesHere;AddFieldValueGoesHere;true]
        $author[AuthorTextGoesHere;https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-caves-and-cliffs-supprt-as-well-as-discord_5.png]
        $thumbnail[https://my.mcpedl.com/storage/texturepacks/3327/images/kellys-minecraft-vanilla-rtx-conversion-pack-clear-water-and-another-addon_8.png]
        $image[https://images.nvidia.com/geforce/news/minecraft-rtx-february-2021-player-worlds-roundup/Kelly-3.jpg]
    
        $addButton[1;label;primary;1;false;]
        $addButton[1;label;secondary;2;false;]
        $addButton[1;label;success;3;false;]
        $addButton[1;label;danger;4;false;]
        $addButton[1;label;link;https://lightslicergp.gitbook.io/lightslicergpbotv3/;false;]
        $addButton[2;label;primary;6;true;]
        $addButton[2;label;secondary;7;true;]
        $addButton[2;label;success;8;true;]
        $addButton[2;label;danger;9;true;]
        $addButton[2;label;link;https://lightslicergp.gitbook.io/lightslicergpbotv3/;true;]
        `, //bottom one is $image, top right one is $thumbnail, top left is $author
    },
  ];