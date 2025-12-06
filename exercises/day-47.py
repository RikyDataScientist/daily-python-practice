"""
🧠 Challenge: Find The Parity Outlier
🔗 Link: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-06

📝 Instruction:
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

💡 Example:
>>> [2, 4, 0, 100, 4, 11, 2602, 36]
11 (the only odd number)
>>> [160, 3, 1719, 19, 11, 13, -21]
160 (the only even number)
"""

# ✨ Your Solution
def find_outlier(integers):
    odd = [i for i in integers if i % 2 != 0]
    even = [i for i in integers if i % 2 == 0]
    return odd[0] if len(odd) < len(even) else even[0]


# ✅ Test Cases
if __name__ == "__main__":
    print(find_outlier([3, 2, 4, 6, 14, 16]))  # 3

# 📝 Note
"""
This problem can be solved efficiently by separating the integers into odd and even lists using list comprehensions.
The outlier is determined by checking which list has only one element.
"""
