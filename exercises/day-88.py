"""
🧠 Challenge: Build Tower
🔗 Link: https://www.codewars.com/kata/576757b1df89ecf5bd00073b/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-03

📝 Instruction:
Build a pyramid-shaped tower, as an array/list of strings,
given a positive integer number of floors.
A tower block is represented with "*" character.

💡 Example:
>>> tower_builder(5)
['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
"""


# ✨ My Solution
def tower_builder(n_floors):
    result = []
    for i in range(1, n_floors + 1):
        space = ' ' * (n_floors - 1)
        star = '*' * (2 * i - 1)
        word = space + star + space
        result.append(word)
        n_floors -= 1
    return result


# ✅ Test Cases
if __name__ == "__main__":
    print(tower_builder(3))  # ['  *  ', ' *** ', '*****']
