"""
🧠 Challenge: Duplicate Arguments
🔗 Link: https://www.codewars.com/kata/520d9c27e9940532eb00018e
🏷️ Level: 6 kyu
📅 Date: 2025-10-27

📝 Instruction:
Complete the solution so that it returns true if it contains any duplicate argument values, and false otherwise. Any number of arguments may be passed into the function.

The arguments passed in will only be strings or numbers.

💡 Example:
>>> solution(1, 2, 3)
False
>>> solution(1, 2, 3, 2)
True
"""

# ✨ Your Solution
def solution(*n):
    for i in n:
        if n.count(i) > 1:
            return True
    return False


# ✅ Test Cases
if __name__ == "__main__":
    print(solution(1, 2, 3, 3, 4))  # True

# 📝 Note
"""
I still my best performance to train my logis to get clean, efficient, and readable code.
"""
