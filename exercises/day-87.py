"""
🧠 Challenge: Find the missing letter
🔗 Link: https://www.codewars.com/kata/5839edaa6754d6fec10000a2/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-01

📝 Instruction:
Write a method that takes an array of consecutive (increasing) letters
as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter
be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

💡 Example:
>>> find_missing_letter(['b', 'c', 'd', 'f'])
e
"""

# ✨ My Solution
from string import ascii_letters as ascii
def find_missing_letter(chars):
    alphabet = ascii[ascii.find(chars[0]):]
    for i, value in enumerate(chars):
        if value != alphabet[i]:
            return alphabet[i]

# ✅ Test Cases
if __name__ == "__main__":
    print(find_missing_letter(['O', 'Q', 'R', 'S']))  # P
