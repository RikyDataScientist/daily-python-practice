"""
🧠 Challenge: Pokemon Damage Calculator
🔗 Link: https://www.codewars.com/kata/536e9a7973130a06eb000e9f
🏷️ Level: 6 kyu
📅 Date: 2025-11-07

📝 Instruction:
It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula (not the actual one from the game):

damage = 50 * (attack / defense) * effectiveness
Where:

attack = your attack power
defense = the opponent's defense
effectiveness = the effectiveness of the attack based on the matchup (see explanation below)
Effectiveness:

Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.

Super effective: 2x damage
Neutral: 1x damage
Not very effective: 0.5x damage
To prevent this kata from being tedious, you'll only be dealing with four types: fire, water, grass, and electric. Here is the effectiveness of each matchup:

fire > grass

fire < water

fire = electric

water < grass

water < electric

grass = electric

For this kata, any type against itself is not very effective. Also, assume that the relationships between different types are symmetric (if A is super effective against B, then B is not very effective against A).

💡 Example:
>>>  calculate_damage('fire', 'water', 200, 50)
100.0
"""

# ✨ Your Solution
def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness_chart = {
        "fire": {"fire": 0.5, "water": 0.5, "grass": 2, "electric": 1},
        "water": {"fire": 2, "water": 0.5, "grass": 0.5, "electric": 0.5},
        "grass": {"fire": 0.5, "water": 2, "grass": 0.5, "electric": 1},
        "electric": {"fire": 1, "water": 2, "grass": 1, "electric": 0.5}
    }

    return 50 * (attack / defense) * effectiveness_chart[your_type][opponent_type]

# ✅ Test Cases
if __name__ == "__main__":
    print(calculate_damage('fire', 'grass', 100, 10))  # 1000.o

# 📝 Note
"""
I'm so confused for make effectivenesss calculation. But, i got this idea and made me finish this case.
"""
