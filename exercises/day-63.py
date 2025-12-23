"""
🧠 Challenge: Friend or Foe?
🔗 Link: https://www.codewars.com/kata/55b42574ff091733d900002f/python
🏷️ Level: 7 kyu
📅 Date: 2025-12-23

📝 Instruction:
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

💡 Example:
>>> friend(["Ryan", "Kieran", "Jason", "Yous"])
['Ryan', 'Yous']
"""

# ✨ Your Solution
def friend(x):
    return [fr for fr in x if len(fr) == 4]


# ✅ Test Cases
if __name__ == "__main__":
    print(friend(['Gilang', 'Fashah', 'Riku', 'Ria']))
    #  ['Riku']
