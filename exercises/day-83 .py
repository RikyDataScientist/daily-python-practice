"""
🧠 Challenge: Playing with digits
🔗 Link: https://www.codewars.com/kata/5552101f47fc5178b1000050/python
🏷️ Level: 6 kyu
📅 Date: 2026-01-24

📝 Instruction:
Given two positive integers n and p, we want to find a positive integer k, if it exists,
such that the sum of the digits of n raised to consecutive powers starting from p
is equal to k * n.

In other words, writing the digits of n as a, b, c, d, ...,
is there an integer k such that:

(a^p + b^(p+1) + c^(p+2) + d^(p+3) + ...) = n * k

If it is the case, return k.
Otherwise, return -1.

💡 Example:
>>> dig_pow(89, 1)
1
"""

# ✨ My Solution
from math import pow
def dig_pow(n, p):
    lst = []
    for i in str(n):
        lst.append(pow(int(i), p))
        p += 1
    res = sum(lst) / n
    return int(res) if res.is_integer() else -1

# ✅ Test Cases
if __name__ == "__main__":
    print(dig_pow(2345, 6))  # -1
