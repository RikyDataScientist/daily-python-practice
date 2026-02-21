"""
🧠 Challenge: Scramblies
🔗 Link: https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python
🏷️ Level: 5 kyu
📅 Date: 2026-02-21

📝 Instruction:
Complete the function scramble(str1, str2) that returns true if a portion of
str1 characters can be rearranged to match str2, otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

💡 Example:
>>> scramblies('cedewaraaossoqqyt', 'codewars')
True
"""

# ✨ Top Solution
def scramblies(s1, s2):
    for i in set(s2):
        if s1.count(i) < s2.count(i):
            return False
    return True

# ✅ Test Cases
if __name__ == "__main__":
    print(scramblies('katas', 'steak'))
    # False
