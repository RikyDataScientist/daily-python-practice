"""
🧠 Challenge: Validate the Euro bill
🔗 Link: https://www.codewars.com/kata/67fb86b6564f0bd70dc615b1
🏷️ Level: 7 kyu
📅 Date: 2025-10-25

📝 Instruction:
The serial number of every Euro bill contains 2 uppercase latin letters at the start and the following 10 digits.

1. Sum every digit in a serial number.
2. Get the English Alphabetical position of the two letters. (A - 1, B - 2, C - 3 and etc.).
3. Add those numbers to the already existing sum of digits.
4. Sum the result's digits up. If the sum is not 1-digit number, keep summing the new number's digits, until the result is 1-digit number.
If the eventual result equals 7, you're holding a real Euro bill. Otherwise, the bill is fake. Assume that every input matches the requirements of a serial number (2 uppercase latin letters and 10 digits).

💡 Example:
>>> validate_euro("VA0436214792")
True
"""

# ✨ Your Solution
Alphabet = {
 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
 'Y': 25, 'Z': 26
}

def validate_euro(serial_number):
    convert = 0
    for i in serial_number:
        if i.isalpha():
            convert += Alphabet[i]
        else:
            convert += int(i)
    while convert >= 10:
        convert = sum(int(d) for d in str(convert))
    if convert == 7:
        return True
    else:
        return False



# ✅ Test Cases
if __name__ == "__main__":
    # Example test cases
    print(validate_euro("GH0436265752"))  # False

# 📝 Note
"""
I still can't make readable and efficient code in this several days.
"""
