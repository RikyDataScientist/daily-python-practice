"""
🧠 Challenge: Complementary DNA
🔗 Link: https://www.codewars.com/kata/554e4a2f232cdd87d9000038/python
🏷️ Level: 7 kyu
📅 Date: 2026-01-29

📝 Instruction:
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and
carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
Your function receives one side of the DNA (string, except for Haskell);
you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

💡 Example:
>>> DNA_strand("AAAA")
TTTT
"""

# ✨ My Solution
def DNA_strand(dna):
    mapping = {
        'T': 'A',
        'A': 'T',
        'C': 'G',
        'G': 'C'
    }
    return "".join([mapping[c] for c in dna])


# ✅ Test Cases
if __name__ == "__main__":
    print(DNA_strand("AATGC"))  # TTACG
