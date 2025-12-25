"""
🧠 Challenge: Ones and Zeros
🔗 Link: https://www.codewars.com/kata/578553c3a1b8d5c40300037c/python
🏷️ Level: 7 kyu
📅 Date: 2025-12-26

📝 Instruction:
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

💡 Example:
>>> binary_array_to_number([0, 0, 0, 1, 0, 1])
5
"""

# ✨ Your Solution
def binary_array_to_number(arr):
    rev = reversed(arr)
    return sum([2 ** i for i, j in enumerate(rev) if j == 1])


# ✅ Test Cases
if __name__ == "__main__":
    print(binary_array_to_number([1, 1, 0, 1, 0, 1]))  # 53
