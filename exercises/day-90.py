"""
🧠 Challenge: Break camelCase
🔗 Link: https://www.codewars.com/kata/5208f99aee097e6552000148/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-09

📝 Instruction:
Complete the solution so that the function will break up camel casing,
using a space between words.

💡 Example:
>>> solution('camelCaseStatement')
camel Case Statement
"""


# ✨ My Solution
import re
def solution(s):
    return re.sub(r'([A-Z][a-z]*)', r' \1', s)


# ✅ Test Cases
if __name__ == "__main__":
    print(solution('howCanYouLook?'))  # how Can You Look?
