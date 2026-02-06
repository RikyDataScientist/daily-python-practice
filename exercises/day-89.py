"""
🧠 Challenge: Highest Scoring Word
🔗 Link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-06

📝 Instruction:
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

💡 Example:
>>> high('i am the man who cannot be moved')
cannot
"""


# ✨ My Solution
def high(x):
    splt = x.split()
    lst = []
    for i in splt:
        lst.append(sum([ord(j) - 96 for j in i]))
    return splt[lst.index(max(lst))]


# ✅ Test Cases
if __name__ == "__main__":
    print(high('i always make sure what i am doing'))  # always
