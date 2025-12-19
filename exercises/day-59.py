"""
🧠 Challenge: Does my number look big in this?
🔗 Link: https://www.codewars.com/kata/5287e858c6b5a9678200083c/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-19

📝 Instruction:
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).
Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

💡 Example:
>>> narcissistic(3668424905)
False
"""

# ✨ Your Solution
def narcissistic(value):
    number = str(value)
    digit = len(number)
    return value == sum([int(i) ** digit for i in number])


# ✅ Test Cases
if __name__ == "__main__":
    print(narcissistic(89022066769276345560))  # False
