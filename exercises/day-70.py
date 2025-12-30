"""
🧠 Challenge: Convert PascalCase string into snake_case
🔗 Link: https://www.codewars.com/kata/529b418d533b76924600085d
🏷️ Level: 5 kyu
📅 Date: 2025-12-30

📝 Instruction:
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
Lowercase characters can be numbers.
If the method gets a number as input, it should return a string.

💡 Example:
>>> to_underscore("TestProgram7")
test_program7
"""

# ✨ Your Solution
def to_underscore(strng: str) -> str:
    if isinstance(strng, int):
        return str(strng)

    upper_case = [i for i, value in enumerate(strng) if value.isupper()]
    upper_case.append(len(strng))

    lst = [strng[upper_case[i]:upper_case[i + 1]] for i in range(len(upper_case) - 1)]
    return "_".join(i.lower() for i in lst)

import re
def to_underscore(strng: str) -> str:
    pattern = re.compile(r"([0-9a-z])([A-Z])")
    return pattern.sub(r"\1_\2", str(strng)).lower()

# ✅ Test Cases
if __name__ == "__main__":
    print(to_underscore("LeverageOurKnowledgeWithPracticeRegularly"))  # leverage_our_knowledge_with_practice_regularly
