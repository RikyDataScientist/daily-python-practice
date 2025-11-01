"""
🧠 Challenge: Word Challenges at School
🔗 Link: https://www.codewars.com/kata/580be55ca671827cfd000043
🏷️ Level: 6 kyu
📅 Date: 2025-11-01

📝 Instruction:
The principal of a school likes to put challenges to the students related with finding words of certain features. One day she said: "Dear students, the challenge for today is to find a word that has only one vowel and seven consonants but cannot have the letters "y" and "m". I'll give a special award for the first student that finds it." One of the students used his dictionary and spent all the night without sleeping, trying in vain to find the word. The next day, the word had not been found yet. This student observed that the principal has a pattern in the features for the wanted words:

The word should have n vowels, may be repeated, for example: in "engineering", n = 5.
The word should have m consonants, may be repeated also: in "engineering", m = 6.
The word should not have some forbidden letters (in an array), forbid_letters.
Vowels are a, e, i, o, and u.
You will be provided with a list of words, WORD_LIST(python/crystal), wordList(javascript), wordList (haskell), $word_list(ruby), and you have to create the function, wanted_words(), that receives the three arguments in the order given above, wanted_words(n, m, forbid_list) and output an array with the word or an array, having the words in the order given in the pre-loaded list, in the case of two or more words were found.

💡 Example:
>>> wanted_words(1, 7, ["m", "y"])
["strength"]
"""

# ✨ Your Solution
from preloaded import WORD_LIST

def wanted_words(n, m, forbid_let):
    vowel = 'aiueo'
    konsonant = ''.join(chr(i) for i in range(97, 123) if chr(i) not in vowel)

    result = []
    for word in WORD_LIST:
        if any(f in word for f in forbid_let):
            continue
        
        vowel_count = sum(word.count(v) for v in vowel)
        konsonant_count = sum(word.count(v) for v in konsonant)
        
        if vowel_count == n and konsonant_count == m:
            result.append(word)
    return result

# ✅ Test Cases
if __name__ == "__main__":
    print(wanted_words(3, 7, ["m", "y"]))  # ['afterwards', 'background', 'photograph', 'successful', 'understand']

# 📝 Note
"""
May be 6 kyu is still my maximum level because there is problem that i can't solved like this one
"""
