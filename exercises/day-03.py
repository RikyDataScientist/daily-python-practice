"""
🧠 Challenge: International Morse Code Encryption
🔗 Link: https://www.codewars.com/kata/55b8c0276a7930249e00003c
🏷️ Level: 7
📅 Date: 2025-10-23

📝 Instruction:
Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.
Characters should be separated by a single space. Words should be separated by a triple space.
For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
To find out more about Morse Code follow this link: https://en.wikipedia.org/wiki/Morse_code
A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to help convert characters to Morse Code.

💡 Example:
>>> encryption("HELLO WORLD")
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
"""

# ✨ Your Solution
from preloaded import CHAR_TO_MORSE

CHAR_TO_MORSE[" "] = " "
def encryption(string):
    morse_code = ""
    for i in string.upper():
        if i in CHAR_TO_MORSE:
            morse_code = morse_code + CHAR_TO_MORSE[i] + " "
    return morse_code.strip()


# ✅ Test Cases
if __name__ == "__main__":
    # Example test cases
    print(encryption("HELLO WORLD"))  # .... . .-.. .-.. ---   .-- --- .-. .-.. -..

# 📝 Note
"""
There were trouble like i can't how the form of Char_T0_Morse (it's like list or dictionary or what) and my code didn't pass in the codewars test.
So, i see the solution from other and re-attend the train with my code which have adjusted. But, the effect is i don't getting a score.
"""
