"""
🧠 Challenge: WeIrD StRiNg CaSe
🔗 Link: https://www.codewars.com/kata/52b757663a95b11b3d00062d
🏷️ Level: 6 kyu
📅 Date: 2025-12-22

📝 Instruction:
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words.
Words will be separated by a single space(' ').

💡 Example:
>>> to_weird_case("This happen suddenly after i baked a cake")
ThIs HaPpEn SuDdEnLy AfTeR I BaKeD A CaKe
"""

# ✨ Your Solution
def to_weird_case(words):
    result = []
    for i in words.split():
        word = "".join(i[x].upper() if x % 2 == 0 else i[x].lower() for x in range(len(i)))
        result.append(word)
    return " ".join(result)


# ✅ Test Cases
if __name__ == "__main__":
    print(to_weird_case("I always watch sport with my father"))
    # I AlWaYs WaTcH SpOrT WiTh My FaThEr
