"""
🧠 Challenge: Help Kiyo きよ solve her problems LCM Fun!
🔗 Link: https://www.codewars.com/kata/5872bb7faa04282110000124
🏷️ Level: 6 kyu
📅 Date: 2025-11-11

📝 Instruction:
Kiyo has been given a series of problems and she needs your help to solve them!

You will be given a two-dimensional array such as the one below.

a = 
[
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

Remove everything but odd integers from each sub-array.
Sum the remaining odd integers of each sub-array.
Sum of odds ( a[0] = 1 + 3 + 5 + 7 + 9 ) = 25
Find the Least common multiple of the arrays.

 (25, 25, 25, 25, 25, 25, 25, 25, 25)
  ^                                ^ 
  |                                |
a[0]-----------------------------a[8]

example : lcm( 25, 25, 25, 25, 25, 25, 25, 25, 25 ) = 25

example : lcm( 37, 29, 19, 38, 31, 28, 15, 24, 9 ) = 1592632440
Integers are between 0 and 9. Sub-array size is always 9. The number of sub-arrays varies between 9 and 18.

Watch out for non-integers mixed in the arrays. If all arrays are empty return 0.

💡 Example:
>>> kiyo_lcm([
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
])
25
"""

# ✨ Your Solution
import math
from functools import reduce as func
def seq(n):
    result = []
    for value in list(n):
        if len(value) == 0:
            result.append(0)
        else:
            result.append(sum([i if i % 2 == 1 else 0 for i in value if isinstance(i, int)]))
    return tuple(result)

def lcm_(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def kiyo_lcm(a):
    seq_process = seq(a)
    return func(lcm_, seq_process, 1) if seq_process else 0


# ✅ Test Cases
if __name__ == "__main__":
    print(kiyo_lcm([[4, 3, 7, 8, 9, 2, 1, 5, 'c'], [6, 5, 6, 1, 'v', 1, 0, 5, 1], [4, 4, 'c', 7, 6, 6, 3, 6, 7], [1, 7, 7, 'l', 5, 8, 9, 5, 9], [0, 't', 8, 2, 8, 9, 0, 8, 0], [4, 6, 2, 6, 'o', 8, 4, 2, 4], [3, 6, 9, 2, 0, 8, 2, 3, 'u'], [9, 3, 1, 9, 4, 4, 'u', 7, 7], [0, 'n', 9, 0, 0, 0, 9, 2, 2]]))  # 0

# 📝 Note
"""
It's little complicated because i don't get to build lcm function and confirm that into our result list to get their lcm.
"""
