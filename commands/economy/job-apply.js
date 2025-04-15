module.exports = [
  // started 10/10/24
  {
    name: "job apply",
    aliases: ["jobs apply"],
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
