"""
🧠 Challenge: Calculate String Rotation
🔗 Link: https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-21

📝 Instruction:
Write a function that receives two strings and returns n, where n is equal to the number of characters we should shift the first string forward to match the second.
The check should be case sensitive.

For instance, take the strings "fatigue" and "tiguefa".
In this case, the first string has been rotated 5 characters forward to produce the second string, so 5 would be returned.

If the second string isn't a valid rotation of the first string, the method returns -1.

💡 Example:
>>> shifted_diff("eecoff", "coffee")
4
"""

# ✨ Your Solution
def shifted_diff(first, second):
    if first == second:
        return 0
    return (second + second).find(first) if len(first) == len(second) else -1


# ✅ Test Cases
if __name__ == "__main__":
    print(shifted_diff("isn't", "'tisn"))  # 2
