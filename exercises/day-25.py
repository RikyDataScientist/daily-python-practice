"""
🧠 Challenge: Moving Zeros To The End
🔗 Link: https://www.codewars.com/kata/52597aa56021e91c93000cb0
🏷️ Level: 5 kyu
📅 Date: 2025-11-14

📝 Instruction:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

💡 Example:
>>> move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

# ✨ Your Solution
def move_zeros(lst):
    lst = list(lst)
    lst.sort(key=lambda a: a == 0)
    return lst


# ✅ Test Cases
if __name__ == "__main__":
    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]

# 📝 Note
"""
I just realised sort and sorted function are giving output false argument first. It was confused me.
"""
