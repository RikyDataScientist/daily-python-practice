"""
🧠 Challenge: Array.diff
🔗 Link: https://www.codewars.com/kata/523f5d21c841566fde000009/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-03

📝 Instruction:
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

💡 Example:
>>> array_diff([1, 2, 2, 3, 5], [2, 3, 1])
[5]
"""

# ✨ Your Solution
def array_diff(a, b):
    return [i for i in a if i not in b]


# ✅ Test Cases
if __name__ == "__main__":
    print(array_diff([1, 2, 2, 3, 6, 2, 5], [2, 3, 1]))  # [6, 5]

# 📝 Note
"""
I don't have comment for this case.
"""
