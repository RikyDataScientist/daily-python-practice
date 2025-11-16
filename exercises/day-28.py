"""
🧠 Challenge: Bubblesort Once
🔗 Link: https://www.codewars.com/kata/56b97b776ffcea598a0006f2
🏷️ Level: 7 kyu
📅 Date: 2025-11-17

📝 Instruction:
Bubblesort is an inefficient sorting algorithm that is simple to understand and therefore often taught in introductory computer science courses as an example how not to sort a list. Nevertheless, it is correct in the sense that it eventually produces a sorted version of the original list when executed to completion.
Given an array of integers, your function should return a new array equivalent to performing exactly 1 complete pass on the original array. Your function should be pure, i.e. it should not mutate the input array.

💡 Example:
>>> bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]
[7, 5, 3, 1, 2, 4, 6, 8, 9]
"""

# ✨ Your Solution
def bubblesort_once(l):
    l = list(l)
    for j in range(len(l) - 1):
        for i in range(len(l)- j - 1):
            if l[i] > l[i+1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        break
    return l


# ✅ Test Cases
if __name__ == "__main__":
    print(bubblesort_once([9, 2, 4, 5, 1, 7, 3, 10]))  # [2, 4, 5, 1, 7, 3, 9, 10]

# 📝 Note
"""
I'm so curious about data structure and algorithm may in the next day i wanna learn about that.
"""
