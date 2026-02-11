"""
🧠 Challenge: Valid Braces
🔗 Link: https://www.codewars.com/kata/5277c8a221e209d3f6000b56/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-12

📝 Instruction:
Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid

💡 Example:
>>> valid_braces("(({{[[]]}}))")
True
"""

# ✨ My Solution
def valid_braces(string):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i in string:
        if i in '{[(':
            stack.append(i)
        if i in '}])':
            if not stack or stack[-1] != pairs[i]:
                return False
            stack.pop()
    return len(stack) == 0

# 🏆 Other Solution
def validBraces(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''

# ✅ Test Cases
if __name__ == "__main__":
    print(valid_braces("())({}}{()][]["))  # False
