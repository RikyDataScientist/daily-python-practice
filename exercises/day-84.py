"""
🧠 Challenge: Split Strings
🔗 Link: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python
🏷️ Level: 6 kyu
📅 Date: 2026-01-25

📝 Instruction:
Complete the solution so that it splits the string into strings of two
characters in a list/array (depending on the language you use).

If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').

💡 Example:
>>> solution('abcde')
['ab', 'cd', 'e_']
"""

# ✨ My Solution
def solution(s):
    if len(s) % 2 == 1:
        s += '_'
    result = []
    while s != '':
        result.append(s[:2])
        s = s[2:]
    return result

# ✅ Test Cases
if __name__ == "__main__":
    print(solution('Again1'))  # ['Ag', 'ai', 'n1']
