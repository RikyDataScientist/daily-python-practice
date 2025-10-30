"""
🧠 Challenge: Simple sum of pairs
🔗 Link: https://www.codewars.com/kata/5bc027fccd4ec86c840000b7
🏷️ Level: 6 kyu
📅 Date: 2025-10-30

📝 Instruction:
Given an integer n, find two integers a and b such that:

A) a >= 0 and b >= 0
B) a + b = n
C) DigitSum(a) + Digitsum(b) is maximum of all possibilities.  
You will return the digitSum(a) + digitsum(b).

For example:
solve(29) = 11. If we take 15 + 14 = 29 and digitSum = 1 + 5 + 1 + 4 = 11. There is no larger outcome.
n will not exceed 10e10.

💡 Example:
>>> solve(7019)
35
"""

# ✨ Your Solution
from functools import lru_cache

@lru_cache(maxsize=None)
def digit(x):
    y = sum([int(i) for i in str(x)])
    return y

def solve(n):
    max_value = 0
    p = 1
    while p * 10 - 1 <= n:
        p *= 10
    a = p - 1
    b = n - a
    value = digit(a) + digit(b)
    if value > max_value:
        max_value = value
    return max_value

# ✅ Test Cases
if __name__ == "__main__":
    print(solve(24623642))  # 92

# 📝 Note
"""
I can't figure out how to make a and b maximum fastly in code because the logic is so complicated. So, i adjusted my code and idea into ai for understanding the problem.
"""
