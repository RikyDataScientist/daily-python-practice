"""
🧠 Challenge: Only Duplicates
🔗 Link: https://www.codewars.com/kata/5a1dc4baffe75f270200006b/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-20

📝 Instruction:
Given a string, remove any characters that are unique from the string.

💡 Example:
>>> only_duplicates('K58cyUyyyFWy9uHHfNfLk7bzYm6')
yyyyyHHff
"""

# ✨ Your Solution
def only_duplicates(st):
    return "".join([i for i in st if st.count(i) > 1])


# ✅ Test Cases
if __name__ == "__main__":
    print(only_duplicates('CFM4rCmAOkv35HH4N5UrlHHPTARkR'))  # C4rCAk5HH45rHHARkR
