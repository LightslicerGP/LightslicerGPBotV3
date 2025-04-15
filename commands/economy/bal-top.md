---
description: See the top of the monetary leaderboard
---

# #bal top

## Usage

{% hint style="success" %}
\#bal top
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done ig? 10/5/24
  {
    name: "bal top",
    aliases: ["baltop"],
    code: `
      $clientTyping
      $reply[$messageID;true]
    
    
    
      $color[#80ff80]
      $title[
      Global Leaderboard
      ]
      $description[$textSplitMap[MoneyLeaderboard]]
    
    
    
      $textSplit[$globalUserLeaderboard[Money;desc;{top}§{tag}§{value};15;1;Bank];\n]
    `,
  },
  {
    name: "MoneyLeaderboard",
    type: "awaited",
    code: `
      $splitText[1]: $splitText[2] - $$numberSeparator[$splitText[3]]
      $textSplit[$message[1];§]
    `,
  },
];

```
{% endcode %}

{% code title="Discord.py" lineNumbers="true" %}
```python
print("Hello World!")
```
{% endcode %}
