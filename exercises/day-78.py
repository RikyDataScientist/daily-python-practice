"""
🧠 Challenge: Detect Pangram
🔗 Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
🏷️ Level: 6 kyu
📅 Date: 2026-01-14

📝 Instruction:
A pangram is a sentence that contains every single letter of the alphabet at least once.

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.

💡 Example:
>>> is_pangram("The quick brown fox jumps over the lazy dog")
True
"""

# ✨ My Solution
from string import ascii_lowercase

def is_pangram(st):
    counting = [st.lower().count(a) for a in ascii_lowercase]
    return all(x >= 1 for x in counting)


# ✅ Test Cases
if __name__ == "__main__":
    print(is_pangram("This isn't a pangram!"))  # False
