"""
🧠 Challenge: (Ready for) Prime Time
🔗 Link: https://www.codewars.com/kata/521ef596c106a935c0000519
🏷️ Level: 5 kyu
📅 Date: 2025-11-21

📝 Instruction:
We need prime numbers and we need them now!
Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.

💡 Example:
>>> prime(5)
[2,3,5]
"""

# ✨ Your Solution
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    result = []
    for i in range(n + 1):
        if is_prime(i):
            result.append(i)
    return result


# ✅ Test Cases
if __name__ == "__main__":
    print(prime(67))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

# 📝 Note
"""
This case is so easy. I wanna make a project for python and after that maybe i wanna learn anythin else.
"""
