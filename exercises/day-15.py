"""
🧠 Challenge: Categorize New Member
🔗 Link: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
🏷️ Level: 7 kyu
📅 Date: 2025-11-04

📝 Instruction:
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

💡 Example:
>>> open_or_senior([[57, 8], [40, 9]])
['Senior', 'Open']
"""

# ✨ Your Solution
def open_or_senior(data):
    return ['Senior' if (age >= 55 and handicap > 7) else 'Open' for age, handicap in data]

# ✅ Test Cases
if __name__ == "__main__":
    print(open_or_senior([[57, 8], [56, 9], [45, 3]]))  # ['Senior', 'Senior', 'Open']

# 📝 Note
"""
It's too esay if i use unpack and list comprehension
"""
