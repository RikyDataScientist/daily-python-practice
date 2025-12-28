"""
🧠 Challenge: Count the smiley faces!
🔗 Link: https://www.codewars.com/kata/583203e6eb35d7980400002a/python
🏷️ Level: 6 kyu
📅 Date: 2025-12-29

📝 Instruction:
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

💡 Example:
>>> count_smileys([':)', ';(', ';}', ':-D'])
2
"""

# ✨ Your Solution
import re
def count_smileys(arr):
    pattern = re.compile(r"(\:|\;)(\-|\~)?(\)|D)")
    return len([m.group(0) for m in pattern.finditer("".join(arr))])


# ✅ Test Cases
if __name__ == "__main__":
    print(count_smileys([';]', ':[', ';*', ':$', ';-D']))  # 1
