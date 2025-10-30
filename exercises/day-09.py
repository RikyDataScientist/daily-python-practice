"""
🧠 Challenge: Rot13
🔗 Link: https://www.codewars.com/kata/530e15517bc88ac656000716
🏷️ Level: 5 kyu
📅 Date: 2025-10-29

📝 Instruction:
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

💡 Example:
>>> rot13("fahGjga")
snuTwtn
"""

# ✨ Your Solution
def rot13(message):
    rot13_map = {
        'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z',
        'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M',
        'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
        'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'
        }
    result = "".join(rot13_map[i] if i in rot13_map else i for i in message)
    return result

# ✅ Test Cases
if __name__ == "__main__":
    print(rot13("Aku sayang Dia"))  # Nxh fnlnat Qvn

# 📝 Note
"""
It's too easy for 5 kyu
"""
