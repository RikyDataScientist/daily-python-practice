"""
🧠 Challenge: Which are in?
🔗 Link: https://www.codewars.com/kata/550554fd08b86f84fe000a58/python
🏷️ Level: 6 kyu
📅 Date: 2026-01-11

📝 Instruction:
Given two arrays of strings a1 and a2 return a sorted array r in
lexicographical order of the strings of a1 which are substrings of strings of a2.

💡 Example:
>>> in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])
['arp', 'live', 'strong']
"""

# ✨ My Solution
def in_array(array1, array2):
    result = []
    for i in array1:
        for j in array2:
            if i in j and i not in result:
                result.append(i)
    result.sort()
    return result

def in_array(array1, array2):
    return sorted(list({i for i in array1 if any(i in j for j in array2)}))


# ✅ Test Cases
if __name__ == "__main__":
    print(in_array(["ng", "hon", "pe"], ["honey", "pudding", "pending"]))  # ['hon', 'ng', 'pe']
