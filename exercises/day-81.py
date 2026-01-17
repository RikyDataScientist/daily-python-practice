"""
🧠 Challenge: Equal Sides Of An Array
🔗 Link: https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python
🏷️ Level: 6 kyu
📅 Date: 2026-01-17

📝 Instruction:
You are going to be given an array of integers.
Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.

💡 Example:
>>> find_even_index([20, 10, -80, 10, 10, 15, 35])
0
"""

# ✨ My Solution
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1

# ✅ Test Cases
if __name__ == "__main__":
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]))  # 3
