"""
🧠 Challenge: Isograms
🔗 Link: https://www.codewars.com/kata/54ba84be607a92aa900000f1
🏷️ Level: 7 kyu
📅 Date: 2025-10-24

📝 Instruction:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

💡 Example:
>>> is_isogram("Dermatoglyphics")
True
>>> is_isogram("moOse")
False
"""

# ✨ Your Solution
def is_isogram(string):
    y = str(string)
    z = y.lower()
    for i in z:
        if z.count(i) > 1:
            return False
    return True


# ✅ Test Cases
if __name__ == "__main__":
    # Example test cases
    print(is_isogram("FfarisS))  # False

# 📝 Note
"""
I still trouble with if-elif-else and loop. Because it were confusing me and my logic solutin is still messy.
"""
