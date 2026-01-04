"""
🧠 Challenge: RGB To Hex Conversion
🔗 Link: https://www.codewars.com/kata/513e08acc600c94f01000001/python
🏷️ Level: 5 kyu
📅 Date: 2026-01-04

📝 Instruction:
The rgb function is incomplete.
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

💡 Example:
>>> rgb(255, 25, 90)
FF195A
"""

# ✨ Your Solution
def rgb(r, g, b):
    lst = [0 if i < 0 else i if i <= 255 else 255 for i in (r, g, b)]
    R, G, B = lst
    return "{:02X}{:02X}{:02X}".format(R, G, B)


# ✅ Test Cases
if __name__ == "__main__":
    print(rgb(600, 156, 200))  # FF9CC8
