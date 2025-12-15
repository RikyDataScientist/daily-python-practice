"""
🧠 Challenge: Adding ordinal indicator suffixes to numbers
🔗 Link: https://www.codewars.com/kata/52dca71390c32d8fb900002b/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-15

📝 Instruction:
Complete the function which should take a number and return it as a string with the correct ordinal indicator suffix (in English). That is:
 1 ==> "1st"
 2 ==> "2nd"
 3 ==> "3rd"
 4 ==> "4th"
 and so on
For the purposes of this kata, you may assume that the function will always be passed a non-negative integer. If the function is given 0 as an argument, it should return "0" (as a string).

💡 Example:
>>> number_to_ordinal(1)
1st
"""

# ✨ Your Solution
def number_to_ordinal(n: int) -> str:
    if n == 0:
        return '0'

    if n % 100 in (11, 12, 13):
        return str(n) + 'th'

    strng = str(n)
    return (
        strng + 'st' if strng[-1] == '1' else
        strng + 'nd' if strng[-1] == '2' else
        strng + 'rd' if strng[-1] == '3' else
        strng + 'th'
    )


# ✅ Test Cases
if __name__ == "__main__":
    print(number_to_ordinal(145))  # 145th

# 📝 Note
"""
I don't have doubt about this kata
"""
