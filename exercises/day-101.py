"""
🧠 Challenge: Remove duplicate words
🔗 Link: https://www.codewars.com/kata/5b39e3772ae7545f650000fc/python
🏷️ Level: 7 kyu
📅 Date: 2026-03-08

📝 Instruction:
Your task is to remove all duplicate words from a string,
leaving only single (first) words entries.

💡 Example:
>>> remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
alpha beta gamma delta
"""

# ✨ Top Solution
import re
def remove_duplicate_words(s):
    splt = re.split(' ', s)
    no_duplicate = list(dict.fromkeys(splt))
    return " ".join(no_duplicate)

# ✅ Test Cases
if __name__ == "__main__":
    print(remove_duplicate_words("gamma delta delta gamma beta alpha beta alpha"))
    # gamma delta beta alpha
