"""
🧠 Challenge: Extract the domain name from a URL
🔗 Link: https://www.codewars.com/kata/514a024011ea4fb54200004b/python
🏷️ Level: 5 kyu
📅 Date: 2025-12-31

📝 Instruction:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

💡 Example:
>>> domain_name("http://www.zombie-bites.com")
zombie-bites
"""

# ✨ Your Solution
import re
def domain_name(url):
    z = re.compile(r"(https?://)?(www\.)?([^./]+)\.[/a-z]*")
    result = z.search(url)
    return result.group(3)


# ✅ Test Cases
if __name__ == "__main__":
    print(domain_name("http://github.com/carbonfive/raygun"))  # github
