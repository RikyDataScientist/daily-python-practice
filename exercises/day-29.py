"""
🧠 Challenge: Grouped by commas
🔗 Link: https://www.codewars.com/kata/5274e122fc75c0943d000148
🏷️ Level: 6 kyu
📅 Date: 2025-11-18

📝 Instruction:
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

💡 Example:
>>> group_by_commas(1234567)
1,234,567
"""

# ✨ Your Solution
def group_by_commas(n):
    word = str(n)
    result = []
    while len(word) > 3:
        result.append(word[-3:])
        word = word[:-3]
    result.append(word)
    result.reverse()
    return ','.join(result)


# ✅ Test Cases
if __name__ == "__main__":
    print(group_by_commas(1234567890))  # 1,234,567,890

# 📝 Note
"""
This case is so esay for me because it's relating with array and strings maipulations. I still trouble to work with some module.
"""
