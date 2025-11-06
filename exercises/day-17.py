"""
🧠 Challenge: Bit Counting
🔗 Link: https://www.codewars.com/kata/526571aae218b8ee490006f4
🏷️ Level: 6 kyu
📅 Date: 2025-11-06

📝 Instruction:
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

💡 Example:
>>> count_bits(65)
2
"""

# ✨ Your Solution
def bit(n):
    x = n
    z = []
    while x != 0:
        if x % 2 == 0:
            z.append(0)
            x = x // 2
        else:
            z.append(1)
            x = x // 2

    while len(z) < 8:
        z.append(0)
    z.reverse()
    return ''.join(str(i) for i in z)

def count_bits(n):
    bit_number = bit(n)
    return sum(int(i) for i in bit_number if i == "1")

# ✅ Test Cases
if __name__ == "__main__":
    print(count_bits(7665))  # 9

# 📝 Note
"""
It's advancement for yesterday's practise so i just improved my idea with the same topic.
"""
