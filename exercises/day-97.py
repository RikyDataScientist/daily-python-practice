"""
🧠 Challenge: Write Number in Expanded Form
🔗 Link: https://www.codewars.com/kata/5842df8ccbd22792a4000245/python
🏷️ Level: 6 kyu
📅 Date: 2026-02-27

📝 Instruction:
You will be given a number and you will need to return it as a string in Expanded Form.

💡 Example:
>>> expanded_form(2345)
2000 + 300 + 40 + 5
"""

# ✨ Top Solution
def expanded_form(num):
    result = []
    for i, value in enumerate(str(num)):
        if value != '0':
            zero = len(str(num)) - i - 1
            result.append(value + '0' * zero)
    return " + ".join(result)

# ✅ Test Cases
if __name__ == "__main__":
    print(expanded_form(29842740))
    # 20000000 + 9000000 + 800000 + 40000 + 2000 + 700 + 40
