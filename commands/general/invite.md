---
description: Invite the bot to your server
---

# #invite

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#invite
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  {
    name: "invite",
    code: `
      $clientTyping    
      $reply[$messageID;true]
  
  
  
      $color[#80bfff]
      $title[Want to invite me to your own server? Click below!]
      $description[
[Invite me!](https://discord.com/api/oauth2/authorize?client_id=698733140939898957&permissions=8&scope=bot%20applications.commands)
[Support Server](https://discord.gg/3TGX6RA)
      ]
    `,
  },
];
```

{% endcode %}

{% code title="Discord.py" lineNumbers="true" fullWidth="false" %}

```python
print("Hello World!")
```

{% endcode %}
