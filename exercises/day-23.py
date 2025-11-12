"""
🧠 Challenge: Pizza pieces
🔗 Link: https://www.codewars.com/kata/5551dc71101b2cf599000023
🏷️ Level: 6 kyu
📅 Date: 2025-11-12

📝 Instruction:
In her trip to Italy, Elizabeth Gilbert made it her duty to eat perfect pizza. One day she ordered one for dinner, and then some Italian friends appeared at her room. The problem is that there were many people who ask for a piece of pizza at that moment, and she had a knife that only cuts straight.
Given the number of pizza cuts, find the maximum amount of pieces of pizza that you can get (not necessarily of equal size). If the number of cuts is negative, return -1 instead (or Nothing in Haskell).

💡 Example:
>>> max_pizza(3)
7.0
"""

# ✨ Your Solution
def max_pizza(cuts):
    if cuts < 0:
        return -1
    else:
        return 1 + (cuts * (cuts + 1) / 2)


# ✅ Test Cases
if __name__ == "__main__":
    print(max_pizza(8))  # 37.0

# 📝 Note
"""
I don't know how to cut pizza correctly for getting max number. So, i had looking video and it was explaining to me about that algorithm.
I know aritmethic pattern that can solve this case.
"""
