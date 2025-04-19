---
description: Get what the current bump channel is set to
---

# #bump channel

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
module.exports = [
  // Done 4/18/25
  {
    name: "bump channel",
    code: `
      $clientTyping
      $reply[$messageID;true]


  
      $color[#80bfff]
      $title[Bump Channel]
      $description[
        The current bump channel is $getGuildVar[DisboardBumpChannel;$guildID]
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
