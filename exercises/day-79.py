"""
🧠 Challenge: Human Readable Time
🔗 Link: https://www.codewars.com/kata/52685f7382004e774f0001f7/python
🏷️ Level: 5 kyu
📅 Date: 2026-01-15

📝 Instruction:
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

💡 Example:
>>> make_readable(56478)
'15:41:18'
"""

# ✨ My Solution
def make_readable(seconds):
    second = seconds
    hour = 0
    minute = 0

    while second >= 60:
        if second >= 3600:
            hour += 1
            second -= 3600
        elif second >= 60:
            minute += 1
            second -= 60
    return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)


# ✅ Test Cases
if __name__ == "__main__":
    print(make_readable(99000))  # 27:30:00
