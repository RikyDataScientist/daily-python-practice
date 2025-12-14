"""
🧠 Challenge: String Scramble
🔗 Link: https://www.codewars.com/kata/5822d89270ca28c85c0000f3/python
🏷️ Level: 7 kyu
📅 Date: 2025-12-14

📝 Instruction:
Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

💡 Example:
>>> scramble('abcd', [0, 3, 1, 2])
'acdb'
"""

# ✨ Your Solution
def scramble(strng, array):
    result = [""] * len(strng)
    for x, y in zip(strng, array):
        result[y] = x
    return "".join(result)

def scramble(strng, array):
    return "".join(i for _, i in sorted(zip(array, strng)))

# ✅ Test Cases
if __name__ == "__main__":
    print(scramble('sc301s', [4, 0, 3, 1, 5, 2]))  # c0s3s1

# 📝 Note
"""
I put one easy kata for today because i'm so busy
"""
