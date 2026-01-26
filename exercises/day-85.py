"""
🧠 Challenge: Sort the odd
🔗 Link: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python
🏷️ Level: 6 kyu
📅 Date: 2026-01-26

📝 Instruction:
You will be given an array of numbers.
You have to sort the odd numbers in ascending order
while leaving the even numbers at their original positions.

💡 Example:
>>> sort_array([5, 9, 2, 8, 1, 4])
[1, 5, 2, 8, 9, 4]
"""

# ✨ My Solution
def sort_array(s):
    lst = [i for i in s if i % 2 == 1]
    lst.sort()
    for i, value in enumerate(s):
        if value % 2 == 1:
            s[i] = lst[0]
            lst.pop(0)
    return s

def sort_array(s):
    odds = sorted((x for x in s if x % 2 != 0), reverse=True)
    return [odds.pop(0) if x % 2 else x for x in s]

# ✅ Test Cases
if __name__ == "__main__":
    print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))  # [1, 1, 5, 11, 2, 11, 111, 0]
