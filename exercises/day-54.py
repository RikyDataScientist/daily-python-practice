"""
🧠 Challenge: Bracket Duplicates
🔗 Link: https://www.codewars.com/kata/5411c4205f3a7fd3f90009ea/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-13

📝 Instruction:
Create a program that will take in a string as input and, if there are duplicates of more than two alphabetical characters in the string, returns the string with all the extra characters in a bracket.
For example, the input "aaaabbcdefffffffg" should return "aa[aa]bbcdeff[fffff]g".
Please also ensure that the input is a string, and return "Please enter a valid string" if it is not.

💡 Example:
>>> string_parse('aAAabbcdeFFFffffg')
aAAabbcdeFF[F]ff[ff]g
"""

# ✨ Your Solution
def string_parse(strng):
    if not isinstance(strng, str):
        return "Please enter a valid string"

    result = ""
    i = 0
    n = len(strng)

    while i < n:
        alpha = strng[i]
        count = 1

        while i + count < n and strng[i + count] == alpha:
            count += 1

        if count > 2:
            result += alpha * 2 + f"[{alpha * (count - 2)}]"
        else:
            result += alpha * count

        i += count

    return result

# With Groupby module
from itertools import groupby
def string_parse(strng):
    return "".join(
        alpha * 2 + f"[{alpha * (n - 2)}]" if n > 2 else alpha * n
        for alpha, g in groupby(strng)
        for n in [sum(1 for _ in g)]
    ) if isinstance(strng, str) else "Please enter a valid string"


# ✅ Test Cases
if __name__ == "__main__":
    print(string_parse('aAAabbcdeffFfFffg'))  # aAAabbcdeffFfFffg

# 📝 Note
"""
This kata is so complicated for me because its test pass is so different with my first concept.
"""
