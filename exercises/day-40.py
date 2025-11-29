"""
🧠 Challenge: First non-repeating character
🔗 Link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python
🏷️ Level: 5 kyu
📅 Date: 2025-11-29

📝 Instruction:
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("")

💡 Example:
>>> first_non_repeating_letter("Should handle simple cases")
o
"""

# ✨ Your Solution
def first_non_repeating_letter(s):
    s = str(s).strip().replace(" ", "")
    lst = s.lower()

    for i in lst:
        if lst.count(i) == 1:
            index = lst.find(i)
            return s[index]
    return ""


# ✅ Test Cases
if __name__ == "__main__":
    # Example test cases
    print(first_non_repeating_letter("Who is my widdle silly mopy doggy then?"))  # p

# 📝 Note
"""
For strings case maybe i have strong logic for that. But i still have for error issues
"""
