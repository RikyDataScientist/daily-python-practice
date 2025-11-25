"""
🧠 Challenge: Convert a linked list to a string
🔗 Link: https://www.codewars.com/kata/582c297e56373f0426000098/python
🏷️ Level: 7 kyu
📅 Date: 2025-11-25

📝 Instruction:
https://en.wikipedia.org/wiki/Linked_list.
Create a function stringify which accepts an argument list / $list and returns a string representation of the list.
The string representation of the list starts with the value of the current Node, specified by its data / $data / Data property, followed by a whitespace character, an arrow and another whitespace character (" -> "), followed by the rest of the list.
The end of the string representation of a list must always end with null / NULL / None / nil / nullptr / null() ( all caps or all lowercase depending on the language you are undertaking this Kata in ). For example, given the following list

💡 Example:
>>> stringify(Node(1, Node(2, Node(3))))
"1 -> 2 -> 3 -> None"
"""

# ✨ Your Solution
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    lst = []
    x = node
    while x is not None:
        lst.append(x.data)
        x = x.next
    lst.append("None")
    return " -> ".join(str(i) for i in lst)



# ✅ Test Cases
if __name__ == "__main__":
    print(stringify(Node(3, Node(6, Node(9, Node(32, Node(8)))))))  # 3 -> 6 -> 9 -> 32 -> 8 -> None

# 📝 Note
"""
I used class for determine which head and tails in the linked list.
"""
