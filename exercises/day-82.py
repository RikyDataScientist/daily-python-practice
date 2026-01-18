"""
🧠 Challenge: Regex validate PIN code
🔗 Link: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/python
🏷️ Level: 7 kyu
📅 Date: 2026-01-18

📝 Instruction:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

💡 Example:
>>> validate_pin("1234567")
False
"""

# ✨ My Solution
import re
def validate_pin(pin):
    return bool(re.match(r'^([0-9]{4}|[0-9]{6})\Z', pin))

# ✅ Test Cases
if __name__ == "__main__":
    print(validate_pin("1111"))  # True
