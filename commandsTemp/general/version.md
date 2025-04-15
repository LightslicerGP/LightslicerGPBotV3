---
description: Get a reminder of what version this bot is
---

# #version

## Usage

{% hint style="success" %}
\#version
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done 10/6/24
  {
    name: "version",
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
  
      $color[#80bfff]
      $title[
          This version of the bot uses the AOI api to write code easier. My cousin reccomended this to me 2/7/22, so lets see if its easier than normal node.js!
      ]
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
