"""
🧠 Challenge: Array Deep Count
🔗 Link: https://www.codewars.com/kata/596f72bbe7cd7296d1000029/python
🏷️ Level: 6 kyu
📅 Date: 2026-03-11

📝 Instruction:
You are given an array. Complete the function that returns the number of
ALL elements within an array, including any nested arrays.

💡 Example:
>>> deep_count(["x", "y", ["z"]])
4
"""

# ✨ Top Solution
def deep_count(a):
    count = 0
    for item in a:
        count += 1
        if isinstance(item, list):
            count += deep_count(item)
    return count

# ✅ Test Cases
if __name__ == "__main__":
    print(deep_count([1, 3, 'r', ['b', [1, 5, 6, ['o']], True]]))  # 12
