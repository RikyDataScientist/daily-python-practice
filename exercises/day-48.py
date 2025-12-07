"""
🧠 Challenge: Duplicate Encoder
🔗 Link: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-07

📝 Instruction:
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

💡 Example:
>>> duplicate_encode("auliaa")
)((())
"""

# ✨ Your Solution
def duplicate_encode(word):
    word = str(word).lower()
    new_word = ""
    for i in word:
        if word.count(i) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word


# ✅ Test Cases
if __name__ == "__main__":
    print(duplicate_encode("fariss riky pratama"))  # ())))))))(()())()()

# 📝 Note
"""
It's too easy.
"""
