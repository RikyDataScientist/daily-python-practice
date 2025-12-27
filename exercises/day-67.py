"""
🧠 Challenge: Get the Middle Character
🔗 Link: https://www.codewars.com/kata/56747fd5cb988479af000028/python
🏷️ Level: 7 kyu
📅 Date: 2025-12-27

📝 Instruction:
You are going to be given a non-empty string.
Your job is to return the middle character(s) of the string.
If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.

💡 Example:
>>> get_middle("HelloWorld"))
oW
"""

# ✨ Your Solution
def get_middle(s):
    idx = (len(s) + 1) // 2
    return s[idx - 1] + s[idx] if len(s) % 2 == 0 else s[idx - 1]


# ✅ Test Cases
if __name__ == "__main__":
    print(get_middle("Hei Buddy"))  # B
