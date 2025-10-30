"""
🧠 Challenge: Counting Duplicates
🔗 Link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
🏷️ Level: 6 kyu
📅 Date: 2025-10-31

📝 Instruction:
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

💡 Example:
>>> duplicate_count("Indivisibilities")
2
"""

# ✨ Your Solution
def duplicate_count(text):
    y = str(text).lower()
    repeat = []
    amount_of_repeat = []
    for i in y:
        if y.count(i) > 1:
            if i not in repeat:
                repeat.append(i)
                amount_of_repeat.append(i)
            else:
                continue
        else:
            amount_of_repeat.append(0)
    return sum(amount_of_repeat)

def duplicate_count(text):
    y = {i for i in text.lower()}
    return sum([1 if text.lower().count(x) > 1 else 0 for x in y])


# ✅ Test Cases
if __name__ == "__main__":
    print(duplicate_count("PythonDictionaries"))  # 4

# 📝 Note
"""
I'm so focus in one perception for solve this code. So, I change my perception and make code with two version.
"""
