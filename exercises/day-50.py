"""
🧠 Challenge: Take a Ten Minutes Walk
🔗 Link: https://www.codewars.com/kata/54da539698b8a2ad76000228/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-09

📝 Instruction:
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.
Return false otherwise.

💡 Example:
>>> is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
True
"""

# ✨ Your Solution
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    return walk.count('s') == walk.count('n') and walk.count('w') == walk.count('e')


# ✅ Test Cases
if __name__ == "__main__":
    print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # False

# 📝 Note
"""
I still find this problem quite straightforward.
"""
