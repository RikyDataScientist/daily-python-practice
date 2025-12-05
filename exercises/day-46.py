"""
🧠 Challenge: Create Phone Number
🔗 Link: https://www.codewars.com/kata/525f50e3b73515a6db000b83/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-05

📝 Instruction:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

💡 Example:
>>> create_phone_number([2, 3, 4, 1, 2, 1, 2, 3, 4, 3])
(234) 121-2343
"""

# ✨ Your Solution
def create_phone_number(n):
    str1 = "".join(str(i) for i in n[0:3])
    str2 = "".join(str(i) for i in n[3:6])
    str3 = "".join(str(i) for i in n[6:])
    return "({}) {}-{}".format(str1, str2, str3)


# ✅ Test Cases
if __name__ == "__main__":
    print(create_phone_number([2, 4, 5, 6, 2, 7, 8, 4, 5]))  # (245) 627-8456

# 📝 Note
"""
Is this case can use regex to solve? I don't know yet.
"""
