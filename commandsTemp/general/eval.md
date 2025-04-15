---
description: Evaluate code directly
---

# #eval

{% hint style="warning" %}
This command is for admins only!
{% endhint %}

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#command \[code]

* \[code] - required
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // done 10.5.24, made more barebones (no embed)
  {
    name: "eval",
    code: `
      $clientTyping
      $reply[$messageID;true]
  
  
   
      $eval[$message]
  
  
  
      $onlyIf[$authorID==586225258269245538||$authorID==883931596758081556;
        {newEmbed:
          {title:YOU ARE NOT HIM. RELAX.}
          {description:You're not LightslicerGP (nor an admin), and I (the bot) can't make you him sooo..... sorry I guess}
          {color:#80bfff}
        }
        {reply:$messageID:true}
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
