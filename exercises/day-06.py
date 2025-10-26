"""
🧠 Challenge: Stop gninnipS My sdroW!
🔗 Link: https://www.codewars.com/kata/5264d2b162488dc400000001
🏷️ Level: 6 kyu
📅 Date: 2025-10-26

📝 Instruction:
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

💡 Example:
>>> spin_words("Hey fellow warriors")
"Hey wollef sroirraw" 
"""

# ✨ Your Solution
def spin_words(sentence):
    y = sentence.split()
    for i in range(len(y)):
        if len(y[i]) > 4:
            y[i] = y[i][::-1]
    x = ' '.join(y)
    return x

# ✅ Test Cases
if __name__ == "__main__":
    print(spin_words("Hello Buddy i just give your a present"))  # olleH ydduB i just give your a tneserp

# 📝 Note
"""
I just confused how to reverse a string within a list.
"""
