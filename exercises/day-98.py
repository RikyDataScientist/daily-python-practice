"""
🧠 Challenge: Count characters in your string
🔗 Link: https://www.codewars.com/kata/52efefcbcdf57161d4000091/python
🏷️ Level: 6 kyu
📅 Date: 2026-03-01

📝 Instruction:
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

💡 Example:
>>> count('Hello World')
{'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
"""

# ✨ Top Solution
from collections import Counter
def count(s):
    if s == '':
        return {}
    return dict(Counter(s))

# ✅ Test Cases
if __name__ == "__main__":
    print(count('Hello World'))
    # {'A': 1, 'b': 1, 'a': 3, 't': 1, 's': 1}
