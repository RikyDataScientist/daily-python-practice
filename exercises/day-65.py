"""
🧠 Challenge: Find the unique number
🔗 Link: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-25

📝 Instruction:
There is an array with some numbers. All numbers are equal except for one. Try to find it!
It's guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.

💡 Example:
>>> find_uniq([ 1, 1, 1, 2, 1, 1 ])
2
"""

# ✨ Your Solution
from collections import Counter
def find_uniq(arr):
    counter = Counter(arr)
    for k, j in counter.items():
        if j == 1:
            return k


# ✅ Test Cases
if __name__ == "__main__":
    print(find_uniq([2, 2, 2, 2, 6, 3, 3]))  # 6
