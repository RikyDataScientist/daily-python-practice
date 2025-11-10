"""
🧠 Challenge: Find the odd int
🔗 Link: https://www.codewars.com/kata/54da5a58ea159efa38000836
🏷️ Level: 6 kyu
📅 Date: 2025-11-10

📝 Instruction:
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

💡 Example:
>>> find_it([0,1,0,1,0])
0
"""

# ✨ Your Solution
def find_it(seq):
    no_duplicate = set(seq)
    for item in no_duplicate:
        if seq.count(item) % 2 == 1:
            return item

# ✅ Test Cases
if __name__ == "__main__":
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))  # 5

# 📝 Note
"""
This code is so easy for me. Maybe, i should take 5 kyu but i'm not sure i can finish or solve that level.
"""
