---
description: Find a user's information from their ID or username
---

# #whois

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#command (option1) \[option2]

- (option1) - optional
- \[option2] - required
  {% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = {
  // done 10/6/24 thanks to ripplex07, i slightly modified it
  name: "whois",
  code: `
    $reply[$messageID;true]
    $clientTyping

    $color[#80bfff]
    $author[$userDisplayName[$get[user]] and $userGlobalName[$get[user]] and $userNickname[$guildID;$get[user];true];$userAvatar[$get[user]]]
    
    $addField[
      User Role Count;
      $userRolesCount[$get[user]];true]
    
    $addField[
      User Role Color;
      $userRoleColor[$get[user]];true]
    
    $addField[
      User Platform;
      $userPlatform[$get[user]];true]
    
    $addField[
      User Lowest Role;
      <@&$userLowestRole[$get[user]]> ($userLowestRole[$get[user]]);true]
    
    $addField[
      User Highest Role;
      <@&$userHighestRole[$get[user]]> ($userHighestRole[$get[user]]);true]
    
    $addField[
      User Custom Status;
      $userCustomStatus[$guildID;$get[user]];true]
    
    $addField[
      User Banner Color;
      $userBannerColor[$get[user]];true]
    
    $addField[
      User Banner;
      $userBanner[$get[user]];true]
    
    $addField[
      User Badges;
      $userBadges[$get[user];, ];true]
    
    $addField[
      User Avatar;
      $userAvatar[$get[user]];true]
    
    $addField[
      User Status;
      $if[$memberExists[$get[user]]==true;
        $userStatus[$guildId;$get[user]];
        This user isn't on the server
      ];true]
    
    $addField[
      DMs open?;
      $if[$isUserDmEnabled[$get[user]] == True;
        ✅;
        ❌
      ];true]
      
    $addField[
      Is A Bot?;
      $if[$isBot[$get[user]]==true;
        ✅;
        ❌
      ];true]
      
    $addField[
      In Server?;
      $if[$memberExists[$get[user]]==true;
        ✅;
        ❌
      ];true]
    
    $addField[
      Creation Date;
      <t:$truncate[$divide[$creationDate[$get[user];ms];1000]]:R>
      $creationDate[$get[user];date];true]
      
    $addField[
      User ID;
      $get[user];true]
      
    $addField[
      Username;
      $username[$get[user]];true]
    
    $let[user;$findUser[$message;true]]
  `,
};
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
print("Hello World!")
```

{% endcode %}
