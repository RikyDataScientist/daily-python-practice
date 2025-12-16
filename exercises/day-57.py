"""
🧠 Challenge: Rock Paper Scissors!
🔗 Link: https://www.codewars.com/kata/5672a98bdbdd995fad00000f
🏷️ Level: 8 kyu
📅 Date: 2025-12-16

📝 Instruction:
Rules of the "Rock, Paper, Scissors" game are:
Rock beats Scissors,
Scissors beat Paper,
Paper beats Rock,
Two identical moves are a draw.
Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.

💡 Example:
>>> rps('rock', 'paper')
Player 2 won!
"""

# ✨ Your Solution
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    rule = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    p_1 = rule[p1]
    return "Player 1 won!" if p_1 == p2 else "Player 2 won!"


# ✅ Test Cases
if __name__ == "__main__":
    print(rps('rock', 'scissors'))  # Player 1 won!

# 📝 Note
"""
I shocked after seen other people's solution. It made me motivate to train harder.
"""
