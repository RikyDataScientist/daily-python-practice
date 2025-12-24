"""
🧠 Challenge: Unique In Order
🔗 Link: https://www.codewars.com/kata/54e6533c92449cc251001667/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-24

📝 Instruction:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

💡 Example:
>>> unique_in_order('AAAABBBCCDAABBB')
['A', 'B', 'C', 'D', 'A', 'B']
"""

# ✨ Your Solution
import itertools
def unique_in_order(sequence):
    return [i for i, _ in itertools.groupby(sequence)]


# ✅ Test Cases
if __name__ == "__main__":
    print(unique_in_order([1, 2, 2, 4, 4, 5, 2, 1]))  # [1, 2, 4, 5, 2, 1]
