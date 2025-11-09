"""
🧠 Challenge: Calculating with Functions
🔗 Link: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
🏷️ Level: 5 kyu
📅 Date: 2025-11-09

📝 Instruction:
This time we want to write calculations using functions and get the results.
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

💡 Example:
>>> six(divided_by(two()))
3
"""

# ✨ Your Solution
def zero(value=None): return 0 if value == None else value(0)
def one(value=None): return 1 if value == None else value(1)
def two(value=None): return 2 if value == None else value(2)
def three(value=None): return 3 if value == None else value(3)
def four(value=None): return 4 if value == None else value(4)
def five(value=None): return 5 if value == None else value(5)
def six(value=None): return 6 if value == None else value(6)
def seven(value=None): return 7 if value == None else value(7)
def eight(value=None): return 8 if value == None else value(8)
def nine(value=None): return 9 if value == None else value(9)

def plus(y): return lambda x: x + y 
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y


# ✅ Test Cases
if __name__ == "__main__":
    print(nine(times(two())))  # 18

# 📝 Note
"""
I never thought the solution used lambda function to return their number. I still struggle with data structures and algorithm.
"""
