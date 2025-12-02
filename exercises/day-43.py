"""
🧠 Challenge: Who likes it?
🔗 Link: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
🏷️ Level: 6 kyu
📅 Date: 2025-12-02

📝 Instruction:
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item.

💡 Example:
>>> likes(["George", "Alex"])
George and Alex like this
"""

# ✨ Your Solution
def likes(names):
    if len(names) <= 0:
        return 'no one likes this'
    elif len(names) == 1:
        return "".join(names) + " likes this"
    elif len(names) == 2:
        return " and ".join(names) + " like this"
    elif len(names) == 3:
        return ", ".join(names[0:2]) + " and " + str(names[-1]) + " like this"
    else:
        return ", ".join(names[0:2]) + " and " + f"{len(names[2:])} others" + " like this"


# ✅ Test Cases
if __name__ == "__main__":
    print(likes(["George"]))  # George likes this
    print(likes(["George", "Alex"]))  # George and Alex like this
    print(likes(["George", "Alex", "Alexia"]))  # George, Alex and Alexia like this
    print(likes(["George", "Alex", "Alexia", "Martha"]))  # George, Alex and 2 others like this

# 📝 Note
"""
This case have a lot of way to solve. Some person use match, if elif else, and there is who use dictionary.
This case i use simple logic with if, elif, and else.
"""
