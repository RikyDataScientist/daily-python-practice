"""
🧠 Challenge: The Hashtag Generator
🔗 Link: https://www.codewars.com/kata/52449b062fb80683ec000024
🏷️ Level: 5 kyu
📅 Date: 2026-01-03

📝 Instruction:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
- It must start with a hashtag (#).
- All words must have their first letter capitalized, and remaining letters lowercased.
- If the final result is longer than 140 chars it must return false.
- If the input or the result is an empty string it must return false.

💡 Example:
>>> generate_hashtag(" Hello there thanks for trying my Kata")
#HelloThereThanksForTryingMyKata
"""

# ✨ Your Solution
import re
def generate_hashtag(s):
    res = "#" + "".join(i.capitalize() for i in re.findall("[A-Za-z]+", s))
    return res if len(res) <= 140 and s != '' else False


# ✅ Test Cases
if __name__ == "__main__":
    print(generate_hashtag("Hello    World    "))  # #HelloWorld
