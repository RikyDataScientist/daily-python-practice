"""
🧠 Challenge: Highest and Lowest
🔗 Link: https://www.codewars.com/kata/554b4ac871d6813a03000035
🏷️ Level: 7 kyu
📅 Date: 2025-11-27

📝 Instruction:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

💡 Example:
>>> high_and_low("6 7 4 5 3 2 -45")
7 -45
"""

# ✨ Your Solution
def high_and_low(numbers):
    number = [int(a) for a in numbers.split(" ")]
    maxs = number[0]
    mins = number[0]
    for i in number:
        if i > maxs:
            maxs = i
        elif i < mins:
            mins = i
        else:
            pass
    return str(maxs) + " " + str(mins)


# ✅ Test Cases
if __name__ == "__main__":
    print(high_and_low("100 -45 56 176 -189 356 -34 -152"))  # 356 -189

# 📝 Note
"""
I look for easy level because I'm hectic for this week. 
"""
