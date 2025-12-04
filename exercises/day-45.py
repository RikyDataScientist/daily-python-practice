"""
🧠 Challenge: Sum of Digits / Digital Root
🔗 Link: https://www.codewars.com/kata/541c8630095125aba6000c00/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-04

📝 Instruction:
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

💡 Example:
>>> digital_root(3425)
5
"""

# ✨ Your Solution
def digital_root(n):
    n = str(n)
    while len(n) > 1:
        result = sum([int(i) for i in n])
        n = str(result)
    return int(n)


# ✅ Test Cases
if __name__ == "__main__":
    print(digital_root(354267684))  # 9

# 📝 Note
"""
It's easy if i use while loop for solve this case.
"""
