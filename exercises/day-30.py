"""
🧠 Challenge: CamelCase Method
🔗 Link: https://www.codewars.com/kata/587731fda577b3d1b0001196
🏷️ Level: 6 kyu
📅 Date: 2025-11-19

📝 Instruction:
Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

💡 Example:
>>> camel_case("test case")
TestCase
"""

# ✨ Your Solution
def camel_case(s):
    s = str(s).strip().title().replace(" ", '')
    return s


# ✅ Test Cases
if __name__ == "__main__":
    print(camel_case(" camel case word"))  # CamelCaseWord

# 📝 Note
"""
This case is too esay for 6 kyu. I didn't get trouble for this case.
"""
