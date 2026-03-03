"""
🧠 Challenge: Sums of Parts
🔗 Link: https://www.codewars.com/kata/5ce399e0047a45001c853c2b/python
🏷️ Level: 6 kyu
📅 Date: 2026-03-03

📝 Instruction:
The function parts_sums (or its variants in other languages) will take as
parameter a list ls and return a list of the sums of its parts as defined above.

💡 Example:
>>> parts_sums([20, 20, 19, 16, 10, 0])
[85, 65, 45, 26, 10, 0, 0]
"""

# ✨ Top Solution
def parts_sums(ls):
    ls.reverse()
    result = [0]
    for i, value in enumerate(ls):
        result.append(result[i] + value)
    result.reverse()
    return result

# ✅ Test Cases
if __name__ == "__main__":
    print(parts_sums([67, 54, 33, 21, 11, 13]))  # [199, 132, 78, 45, 24, 13, 0]
