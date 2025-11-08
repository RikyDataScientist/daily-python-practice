"""
🧠 Challenge: Replace With Alphabet Position
🔗 Link: https://www.codewars.com/kata/546f922b54af40e1e90001da/python
🏷️ Level: 6 kyu
📅 Date: 2025-11-08

📝 Instruction:
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

💡 Example:
>>> alphabet_position('The beautiful scenery is always here with you')
20 8 5 2 5 1 21 20 9 6 21 12 19 3 5 14 5 18 25 9 19 1 12 23 1 25 19 8 5 18 5 23 9 20 8 25 15 21
"""

# ✨ Your Solution
def alphabet_position(text):
    text = text.lower()
    return " ".join([str(ord(i) - 96) for i in text if i.isalpha()])


# ✅ Test Cases
if __name__ == "__main__":
    print(alphabet_position('My life is not full without you'))  # 13 25 12 9 6 5 9 19 14 15 20 6 21 12 12 23 9 20 8 15 21 20 25 15 21

# 📝 Note
"""
It's quitely hard if i don't know about ord function. BUt, yeah i did better today.
"""
