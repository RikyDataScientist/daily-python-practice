"""
🧠 Challenge: Not very secure
🔗 Link: https://www.codewars.com/kata/526dbd6c8c0eb53254000110
🏷️ Level: 5 kyu
📅 Date: 2026-01-01

📝 Instruction:
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:
At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore

💡 Example:
>>> alphanumeric("hello world_")
False
"""

# ✨ Your Solution
import re
def alphanumeric(password: str) -> bool:
    if len(password) == 0:
        return False
    pattern = re.findall(r"[^A-Za-z0-9]", password)
    return False if len(pattern) > 0 else True


# ✅ Test Cases
if __name__ == "__main__":
    print(alphanumeric("PassW0rd"))  # True
