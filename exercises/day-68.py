"""
🧠 Challenge: Disemvowel Trolls
🔗 Link: https://www.codewars.com/kata/52fba66badcd10859f00097e
🏷️ Level: 7 kyu
📅 Date: 2025-12-28

📝 Instruction:
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

💡 Example:
>>> disemvowel("This website is for losers LOL!")
"Ths wbst s fr lsrs LL!"
"""

# ✨ Your Solution
import re
def disemvowel(string_):
    return re.sub(
        r"[aiueoAIUEO]",
        "",
        string_
    )


# ✅ Test Cases
if __name__ == "__main__":
    print(disemvowel("I wanna make a rocket when I be adult"))  # wnn mk  rckt whn  b dlt
