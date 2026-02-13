"""
🧠 Challenge: Is a number prime?
🔗 Link: https://www.codewars.com/kata/5262119038c0985a5b00029f/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-13

📝 Instruction:
Define a function that takes an integer argument and returns a logical
value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater
than 1 that has no positive divisors other than 1 and itself.

💡 Example:
>>> is_prime(5)
True
"""

# ✨ My Solution
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# ✅ Test Cases
if __name__ == "__main__":
    print(is_prime(6))  # False
