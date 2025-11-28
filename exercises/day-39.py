"""
🧠 Challenge: Complete The Pattern #7 - Cyclical Permutation
🔗 Link: https://www.codewars.com/kata/557592fcdfc2220bed000042/python
🏷️ Level: 7 kyu
📅 Date: 2025-11-28

📝 Instruction:
You have to write a function which creates the following pattern (See Examples) upto desired number of rows.
If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

💡 Example:
>>> pattern(7)
1234567
2345671
3456712
4567123
5671234
6712345
7123456
"""

# ✨ Your Solution
def pattern(n: int) -> str:
    if n <= 0:
        return ""
    else:
        lst = [i for i in range(1, n + 1)]
        result = []
        for i in range(len(lst)):
            result.append("".join(str(a) for a in lst))
            lst.insert(len(lst), lst[0])
            lst.pop(0)
        return "\n".join(result)


# ✅ Test Cases
if __name__ == "__main__":
    print(pattern(19))
    # 12345678910111213141516171819
    # 23456789101112131415161718191
    # 34567891011121314151617181912
    # 45678910111213141516171819123
    # 56789101112131415161718191234
    # 67891011121314151617181912345
    # 78910111213141516171819123456
    # 89101112131415161718191234567
    # 91011121314151617181912345678
    # 10111213141516171819123456789
    # 11121314151617181912345678910
    # 12131415161718191234567891011
    # 13141516171819123456789101112
    # 14151617181912345678910111213
    # 15161718191234567891011121314
    # 16171819123456789101112131415
    # 17181912345678910111213141516
    # 18191234567891011121314151617
    # 19123456789101112131415161718

# 📝 Note
"""
I don't have enough time for practise so i choose easy case.
"""
