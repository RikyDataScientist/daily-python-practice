"""
🧠 Challenge: Build a pile of Cubes
🔗 Link: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-15

📝 Instruction:
Build a pile of cubes where each cube has a decreasing volume.

The bottom cube has a volume of n³, the next cube has a volume of (n−1)³,
and so on until the top cube has a volume of 1³.

Given the total volume m of the pile, determine whether there exists
a positive integer n such that:

    n³ + (n−1)³ + (n−2)³ + ... + 1³ = m

If such an integer n exists, return n.
Otherwise, return -1.

Parameters:
    m (int): The total volume of the cube pile.

Returns:
    int: The number of cubes (n) if a valid solution exists, otherwise -1.

💡 Example:
>>> find_nb(1071225)
45
"""

# ✨ My Solution
from math import isqrt
def find_nb(m):
    k = isqrt(m)
    if k * k != m:
        return -1

    D = 1 + 8 * k
    sqrt_d = isqrt(D)
    if sqrt_d * sqrt_d != D:
        return -1

    n = (-1 + sqrt_d) // 2
    return n if n * (n + 1) // 2 == k else -1

# ✅ Test Cases
if __name__ == "__main__":
    print(find_nb(135440716410000))  # 4824
