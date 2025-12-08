"""
🧠 Challenge: Convert string to camel case
🔗 Link: https://www.codewars.com/kata/517abf86da9663f1d2000003/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-08

📝 Instruction:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.

💡 Example:
>>> to_camel_case("the_stealth_warrior")
theStealthWarrior
"""

# ✨ Your Solution
def to_camel_case(text):
    if text == "":
        return ""
    word = text.replace("_", " ").replace("-", " ").split(" ")
    return word[0] + "".join(i.capitalize() for i in word[1:])


# ✅ Test Cases
if __name__ == "__main__":
    print(to_camel_case("A-B-C"))  # ABC

# 📝 Note
"""
This case is too easy to solve.
"""
