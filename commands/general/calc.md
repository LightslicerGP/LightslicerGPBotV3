---
description: Do some math calculation
---

# #calc

## Usage

{% hint style="success" %}
\#calc \[option2]

- \[equation] - required
  {% endhint %}

## Code

{% hint style="warning" %}
| means OR, & means AND, ^ means XOR, implied multiplication doesnt work
{% endhint %}

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}

```javascript
module.exports = [
  // DONT GET RID OF INDEX!!!!!
  // Done 4/18/25
  {
    name: "calc",
    code: `
        $clientTyping
        $reply[$messageID;true]



        $color[1;#80bfff]
        $title[1;
            Here is your result:
        ]
        $description[1;
            $math[$replaceText[$noMentionMessage;x;*]]
        ]
        $footer[
| means OR, & means AND, ^ means XOR,
implied multiplication doesnt work
        ]



        $onlyIf[$message!=;{"embeds":"
            {newEmbed:
            {title:Please include some expression to calculate!}
            {color:#80bfff}}",
            "reply": {"messageReference": "$messageID"}
        }]
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
