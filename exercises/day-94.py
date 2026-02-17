"""
🧠 Challenge: Remove anchor from URL
🔗 Link: https://www.codewars.com/kata/51f2b4448cadf20ed0000386/python
🏷️ Level: 7 kyu
📅 Date: 2026-02-17

📝 Instruction:
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

💡 Example:
>>> remove_url_anchor("www.codewars.com#about")
www.codewars.com
"""

# ✨ My Solution
def remove_url_anchor(url):
    return __import__('re').sub(r'#.*$', '', url)

# ✅ Test Cases
if __name__ == "__main__":
    print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
    # www.codewars.com/katas/?page=1
