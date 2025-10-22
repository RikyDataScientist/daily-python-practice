"""
🧠 Challenge: Descending Order
🔗 Link: https://www.codewars.com/kata/5467e4d82edf8bbf40000155
🏷️ Level: 7 kyu
📅 Date: 2025-10-22

📝 Instruction:
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

💡 Example:
>>> descending_order(145263)
654321
"""

# ✨ Your Solution
def descending_order(num):
    x = str(num)
    y =[]
    for i in x:
        y.append(i)
    y.sort(reverse=True)
    z = ''.join(y)
    w = int(z)
    return w

# ✅ Test Cases
if __name__ == "__main__":
    print(descending_order(4532))  # 5432

# 📝 Note
"""
I always wonder why i'm connecting every case with list and that like spam. I don't get a solution with other methods except list. But, i still try it. 
"""
