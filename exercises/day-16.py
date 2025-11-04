"""
🧠 Challenge: Binary Addition
🔗 Link: https://www.codewars.com/kata/551f37452ff852b7bd000139
🏷️ Level: 7 kyu
📅 Date: 2025-11-05

📝 Instruction:
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.

💡 Example:
>>> add_binary(1, 2)
'11' in binary number
"""

# ✨ Your Solution
def add_binary(a, b):
    bit_convert = []
    sum_number = a + b
    while sum_number != 0:
        if sum_number % 2 != 0:
            bit_convert.append(1)
        else:
            bit_convert.append(0)
        sum_number = sum_number // 2
    bit_convert.reverse()
    return ''.join(str(i) for i in bit_convert)

# ✅ Test Cases
if __name__ == "__main__":
    print(add_binary(45, 76))  # 1111001

# 📝 Note
"""
I ever try this code before that's why i can solve this code fluently.
"""
