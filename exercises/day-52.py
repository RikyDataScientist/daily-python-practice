"""
🧠 Challenge: Simple Pig Latin
🔗 Link: https://www.codewars.com/kata/520b9d2ad5c005041100000f/python
🏷️ Level: 5 kyu
📅 Date: 2025-12-11

📝 Instruction:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

💡 Example:
>>> pig_it('Pig latin is cool')
igPay atinlay siay oolcay
"""

# ✨ Your Solution
def pig_it(text):
    return " ".join([word[1:] + word[0] + "ay" if word.isalpha() else word for word in text.split(" ")])


# ✅ Test Cases
if __name__ == "__main__":
    print(pig_it("Hello My Best Friend"))  # elloHay yMay estBay riendFay

# 📝 Note
"""
For 5 kyu it's a simple problem of string manipulation. 
"""
