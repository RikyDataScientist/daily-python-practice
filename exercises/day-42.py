"""
🧠 Challenge: Multiples of 3 or 5
🔗 Link: https://www.codewars.com/kata/514b92a657cdc65150000006
🏷️ Level: 6 kyu
📅 Date: 2025-12-01

📝 Instruction:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If a number is a multiple of both 3 and 5, only count it once.

💡 Example:
>>> solution(6)
8
"""

# ✨ Your Solution
def solution(number):
    return sum([i for i in range(1, number) if (i % 3 == 0) or (i % 5 == 0)])


# ✅ Test Cases
if __name__ == "__main__":
    print(solution(12))  # 33

# 📝 Note
"""
I don't have trouble for this case.
"""
