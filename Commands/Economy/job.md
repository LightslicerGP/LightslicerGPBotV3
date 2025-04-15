---
description: Get a list of jobs
---

# #job

{% hint style="danger" %}
This command is still in development!
{% endhint %}

## Usage

{% hint style="success" %}
\#job
{% endhint %}

## Code

{% code title="AOI.js" lineNumbers="true" fullWidth="false" %}
```javascript
module.exports = [
  // started 10/6/24
  {
    name: "job",
    aliases: ["jobs"],
    code: `
        $clientTyping
        $reply[$messageID;true]
      
        $color[#80ff80]
        $title[
          Here are a list of Jobs:
        ]
        $description[
1. $10/hr - Fast Food Worker
2. $20/hr - Teacher
3. $30/hr - Paralegal
4. $40/hr - Software Developer
5. $50/hr - Project Manager
6. $60/hr - Lawyer
7. $70/hr - Dentist
8. $80/hr - Doctor
9. $90/hr - Investment Banker
10. $100/hr - Chief Executive Officer
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
