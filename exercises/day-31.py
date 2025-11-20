"""
🧠 Challenge: Letterbox Paint-Squad
🔗 Link: https://www.codewars.com/kata/597d75744f4190857a00008d
🏷️ Level: 7 kyu
📅 Date: 2025-11-20

📝 Instruction:
You and a group of friends are earning some extra money in the school holidays by re-painting the numbers on people's letterboxes for a small fee.
Since there are 10 of you in the group each person just concentrates on painting one digit! For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...
But at the end of the day you realise not everybody did the same amount of work.
To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.
Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.

💡 Example:
>>> paint_letterboxes(125, 132)
[1, 9, 6, 3, 0, 1, 1, 1, 1, 1]
"""

# ✨ Your Solution
def paint_letterboxes(start, finish):
    z = "".join(str(i) for i in range(start, finish + 1))
    result = []
    for number in range(10):
        if str(number) in z:
            result.append(z.count(str(number)))
        else:
            result.append(0)
    return result


# ✅ Test Cases
if __name__ == "__main__":
    print(paint_letterboxes(345, 756))  # [81, 81, 81, 136, 186, 189, 182, 138, 81, 81]

# 📝 Note
"""
For this case, i can solve that fluently because the algorithm is so esay and i found briliant method for this case.
"""
