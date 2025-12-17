"""
🧠 Challenge: Run-length encoding
🔗 Link: https://www.codewars.com/kata/546dba39fa8da224e8000467/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-17

📝 Instruction:
Your task is to write such a run-length encoding.
For a given string, return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ], such that one can reconstruct the original string by replicating the character sx ix times and concatening all those strings.
Your run-length encoding should be minimal, ie. for all i the values si and si+1 should differ.


💡 Example:
>>> run_length_encoding("faaBBaBjf")
[[1, 'f'], [2, 'a'], [2, 'B'], [1, 'a'], [1, 'B'], [1, 'j'], [1, 'f']]
"""

# ✨ Your Solution
def run_length_encoding(s):
    if not s:
        return []

    result = []
    count = 1
    current = s[0]

    for i in s[1:]:
        if current == i:
            count += 1
        else:
            result.append([count, current])
            count = 1
            current = i
    result.append([count, current])

    return result

from itertools import groupby
def run_length_encoding(s):
    return [(a, b) for a, b in groupby(s)]

# ✅ Test Cases
if __name__ == "__main__":
    print(run_length_encoding("welcome to out office"))  # [[1, 'w'], [1, 'e'], [1, 'l'], [1, 'c'], [1, 'o'], [1, 'm'], [1, 'e'], [1, ' '], [1, 't'], [1, 'o'], [1, ' '], [1, 'o'], [1, 'u'], [1, 't'], [1, ' '], [1, 'o'], [2, 'f'], [1, 'i'], [1, 'c'], [1, 'e']]

# 📝 Note
"""
This solution uses a single pass through the string (O(n) time). It ensures minimal encoding by grouping only consecutive identical characters.
"""
