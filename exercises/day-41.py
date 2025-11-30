"""
🧠 Challenge: Decode the Morse code
🔗 Link: https://www.codewars.com/kata/54b724efac3d5402db00065e
🏷️ Level: 6 kyu
📅 Date: 2025-11-30

📝 Instruction:
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
NOTE: Extra spaces before or after the code have no meaning and should be ignored.
In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS, that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.
Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

💡 Example:
>>> decode_morse(".... . -.--   .--- ..- -.. .")
HEY JUDE
"""

# ✨ Your Solution
MORSE_CODE = {
    # Letters
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",

    # Numbers
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",

    # Punctuation
    ".-.-.-": ".",     # period
    "--..--": ",",     # comma
    "..--..": "?",     # question mark
    ".----.": "'",     # apostrophe
    "-.-.--": "!",     # exclamation
    "-..-.": "/",      # slash
    "-.--.": "(",      # left parenthesis
    "-.--.-": ")",     # right parenthesis
    ".-...": "&",      # ampersand
    "---...": ":",     # colon
    "-.-.-.": ";",     # semicolon
    "-...-": "=",      # equals
    ".-.-.": "+",      # plus
    "-....-": "-",     # hyphen
    "..--.-": "_",     # underscore
    ".-..-.": "\"",    # quotation mark
    "...-..-": "$",    # dollar sign
    ".--.-.": "@",     # at symbol
}

def decode_morse(morse_code):
    words = morse_code.strip().split("   ")
    result = []
    for word in words:
        letters = "".join(MORSE_CODE[i] for i in word.split(" "))
        result.append(letters)
    return " ".join(result)


# ✅ Test Cases
if __name__ == "__main__":
    print(decode_morse('      ... --- ... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))
    # SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.

# 📝 Note
"""
I need to practice more in order get a clean code.
"""
