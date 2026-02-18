"""
🧠 Challenge: String incrementer
🔗 Link: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python
🏷️ Level: 5 kyu
📅 Date: 2026-02-19

📝 Instruction:
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.

💡 Example:
>>> increment_string('Faris')
Faris1
"""

# ✨ My Solution
def increment_string(string: str):
    matched = __import__('re').search(r'(\d+)$', string)
    if matched:
        number = matched.group(1)
        return string[:matched.start()] + str(int(number) + 1).zfill(len(number))
    else:
        return string + '1'

# ✅ Test Cases
if __name__ == "__main__":
    print(increment_string('fakiehp0009'))
    # fakiehp0010
