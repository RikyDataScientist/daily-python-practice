"""
🧠 Challenge: Conway's Look and Say - Generalized
🔗 Link: https://www.codewars.com/kata/530045e3c7c0f4d3420001af/python
🏷️ Level: 5 kyu
📅 Date: 2025-11-24

📝 Instruction:
Your task is to create a function that will take an integer and return the result of the look-and-say function on that integer. This should be a general function that takes as input any positive integer, and returns an integer; inputs are not limited to the sequence which starts with "1".
Conway's Look-and-say sequence goes like this:
Start with a number.
Look at the number, and group consecutive digits together.
For each digit group, say the number of digits, then the digit itself.
This can be repeated on its result to generate the sequence.

💡 Example:
>>> look_say(1112233221)
3122232211
"""

# ✨ Your Solution
def look_say(n):
    number = [int(i) for i in str(n)]
    result = []
    counter = number[0]
    count = 1
    for i in range(1, len(number)):
        if counter == number[i]:
            count += 1
        else:
            result.append((count, counter))
            counter = number[i]
            count = 1
    result.append((count, counter))
    end = "".join(str(x) + str(y) for x, y in result)
    return int(end)


# ✅ Test Cases
if __name__ == "__main__":
    print(look_say(44444444433322211155557788999987))  # 94333231452728491817

# 📝 Note
"""
I made a mistake which put digit and count in wrong way. That's making a wrong output
"""
