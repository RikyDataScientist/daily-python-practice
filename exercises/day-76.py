"""
🧠 Challenge: Directions Reduction
🔗 Link: https://www.codewars.com/kata/550f22f4d758534c1100025a/python
🏷️ Level: 5 kyu
📅 Date: 2026-01-05

📝 Instruction:
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort.
Since this is the wild west, with dreadful weather and not much water,
it's important to save yourself some energy, otherwise you might die of thirst!
How I crossed a mountainous desert the smart way.

Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
The OCaml version takes a list of type direction = | North | South | East | West.

💡 Example:
>>> dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
['WEST']
"""

# ✨ Your Solution
def dir_reduc(arr):
    opposite = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST"
    }

    result = []
    for i in arr:
        if result and opposite[i] == result[-1]:
            result.pop()
        else:
            result.append(i)

    return result


# ✅ Test Cases
if __name__ == "__main__":
    print(dir_reduc(["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"]))
    # ['NORTH', 'EAST']
