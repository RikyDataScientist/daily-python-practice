"""
🧠 Challenge: Multiplication table for number
🔗 Link: https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
🏷️ Level: 8 kyu
📅 Date: 2025-11-03

📝 Instruction:
Your goal is to return multiplication table for number that is always an integer from 1 to 10.
P. S. You can use \n in string to jump to the next line.
Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about the format, look at the sample tests.

💡 Example:
>>> multi_table(5)
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
"""

# ✨ Your Solution
def multi_table(number):
    result = []
    for i in range(1, 11):
        result.append(f"{i} * {number} = {i * number}")
    return '\n'.join(result)


# ✅ Test Cases
if __name__ == "__main__":
    print(multi_table(15))

# 1 * 15 = 15
# 2 * 15 = 30
# 3 * 15 = 45
# 4 * 15 = 60
# 5 * 15 = 75
# 6 * 15 = 90
# 7 * 15 = 105
# 8 * 15 = 120
# 9 * 15 = 135
# 10 * 15 = 150

# 📝 Note
"""
For this part, i can create a code but still not readable. I want to train function deeply and after that, i'm gonna learning OOP.
"""
