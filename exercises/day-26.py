"""
🧠 Challenge: Sum of Pairs
🔗 Link: https://www.codewars.com/kata/54d81488b981293527000c8f
🏷️ Level: 5 kyu
📅 Date: 2025-11-16

📝 Instruction:
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.
Negative numbers and duplicate numbers can and will appear.

💡 Example:
>>> sum_pairs([1, 4, 8, 7, 3, 15], 8)
[1, 7]
"""

# ✨ Your Solution
def sum_pairs(ints, s):
    no_duplicate = set()
    for value in ints:
        result = s - value
        if result in no_duplicate:
            return [result, value]
        no_duplicate.add(value)
    return None


# ✅ Test Cases
if __name__ == "__main__":
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))  # [3, 7]

# 📝 Note
"""
There is no comment for this kata
"""
