"""
🧠 Challenge: Don't give me five!
🔗 Link: https://www.codewars.com/kata/5813d19765d81c592200001a
🏷️ Level: 7 kyu
📅 Date: 2025-11-16

📝 Instruction:
In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

💡 Example:
>>> dont_give_me_five(1,9)
8
"""

# ✨ Your Solution
def dont_give_me_five(start,end):
    y = [str(i) for i in range(start, end + 1) if not '5' in str(i)]
    return len(y)


# ✅ Test Cases
if __name__ == "__main__":
    print(dont_give_me_five(4,80))  # 60

# 📝 Note
"""
In this case, i didn't get trouble or struggle because i can figure out what i must do for solve this case.
"""
