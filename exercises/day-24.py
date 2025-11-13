"""
🧠 Challenge: Product of consecutive Fib numbers
🔗 Link: https://www.codewars.com/kata/5541f58a944b85ce6d00006a
🏷️ Level: 5 kyu
📅 Date: 2025-11-13

📝 Instruction:
The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:
F(n) * F(n + 1)= prod
Your function takes an integer (prod) and returns an array/tuple (check the function signature/sample tests for the return type in your language):
if F(n) * F(n+1) = prod:
(F(n), F(n+1), true)
If you do not find two consecutive F(n) verifying F(n) * F(n+1) = prod:
(F(n), F(n+1), false)
where F(n) is the smallest one such as F(n) * F(n+1) > prod.

💡 Example:
>>> product_fib(4895)
[55, 89, True]
"""

# ✨ Your Solution
def product_fib(_prod):
    a, b = 0, 1
    while a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]


# ✅ Test Cases
if __name__ == "__main__":
    print(product_fib(5895))  # [89, 144, False]

# 📝 Note
"""
This code is so easy to solve. I can figure out what the problem is.
"""
