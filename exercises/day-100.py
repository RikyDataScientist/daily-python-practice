"""
🧠 Challenge: Valid Phone Number
🔗 Link: https://www.codewars.com/kata/525f47c79f2f25a4db000025/python
🏷️ Level: 6 kyu
📅 Date: 2026-03-05

📝 Instruction:
Write a function that accepts a string, and returns true
if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots
will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

💡 Example:
>>> valid_phone_number('(123) 456-7890')
True
"""

# ✨ Top Solution
def valid_phone_number(phone_number: str):
    return bool(__import__('re').search(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number))

# ✅ Test Cases
if __name__ == "__main__":
    print(valid_phone_number('234 328-9867'))  # False
