"""
🧠 Challenge: Your order, please
🔗 Link: https://www.codewars.com/kata/55c45be3b2079eccff00010f/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-12

📝 Instruction:
Your task is to sort a given string.
Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers

💡 Example:
>>> order("is2 Thi1s T4est 3a")
"Thi1s is2 3a T4est"
"""

# ✨ Your Solution
def order(sentence):
    if len(sentence) == 0:
        return ''
    order = sentence.split()
    result = []
    for i in range(1, len(order) + 1):
        for x in order:
            if str(i) in x:
                result.append(x)
            else:
                continue
    return " ".join(result)

# 🏆Best Solution
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda w: sorted(w)))

# ✅ Test Cases
if __name__ == "__main__":
    print(order("3th ha7 uaa6fu bhf2 bnk4j fah1 l5kaj"))  # fah1 bhf2 3th bnk4j uaa6fu ha7

# 📝 Note
"""
Your Note for this practise
"""
