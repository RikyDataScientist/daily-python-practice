"""
🧠 Challenge: Validate Credit Card Number
🔗 Link: https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
🏷️ Level: 6 kyu
📅 Date: 2025-10-28

📝 Instruction:
In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.
Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.

💡 Example:
>>> validate(12314)
False
"""

# ✨ Your Solution
def validate(n):
    number_list = [int(y) for y in str(n)]
    number_invers = reversed(number_list)
    w = [idx * 2 if i % 2 == 1 else idx for i, idx in enumerate(number_invers)]
    x = [(idx - 9) if (idx > 9 and i % 2 == 1) else idx for i, idx in enumerate(w)]
    return False if sum(x) % 10 != 0 else True


# ✅ Test Cases
if __name__ == "__main__":
    print(validate(3645378574126789))  # False

# 📝 Note
"""
I have learned how to write clean code even though i'm still confused about the algorithm especially for scanning. But yeah i did my best.
"""
