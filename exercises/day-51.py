"""
🧠 Challenge: Persistent Bugger.
🔗 Link: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-10

📝 Instruction:
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

💡 Example:
>>> persistence(45)
2
"""

# ✨ Your Solution
def persistence(n):
    number = n
    count = 0
    while number >= 10:
        product = 1
        for i in str(number):
            product *= int(i)
        number = product
        count +=1
    return count


# ✅ Test Cases
if __name__ == "__main__":
    print(persistence(156))  # 2

# 📝 Note
"""
This code is little bit struggled me or am i overwhelmed?
"""
