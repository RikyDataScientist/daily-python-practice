"""
🧠 Challenge: Parse a linked list from a string
🔗 Link: https://www.codewars.com/kata/582c5382f000e535100001a7
🏷️ Level: 6 kyu
📅 Date: 2025-11-26

📝 Instruction:
Create a function parse which accepts exactly one argument string / $string / s / strrep ( or similar, depending on the language ) which is a string representation of a linked list. Your function must return the corresponding linked list, constructed from instances of the Node class/struct/type. The string representation of a list has the following format: the value of the node, followed by a whitespace, an arrow and another whitespace (" -> "), followed by the rest of the linked list. Each string representation of a linked list will end in "null" / "NULL" / "nil" / "nullptr" / "null()" depending on the language you are undertaking this Kata in. For example, given the following string representation of a linked list:
... your function should return:
Note that due to the way the constructor for Node is defined, if a second argument is not provided, the next / $next / Next field is automatically set to null / NULL / nil / nullptr ( or equivalent in your language ). That means your function could also return the following ( if it helps you better visualise what is actually going on ):
Another example: given the following string input:
... your function should return:
If the input string is just "null" / "NULL" / "nil" / "nullptr" / "null()", return null / NULL / nil / nullptr / null() / [] ( or equivalent ).
For the simplicity of this Kata, the values of the nodes in the string representation will always ever be non-negative integers, so the following would not occur: "Hello World -> Goodbye World -> 123 -> null" / "Hello World -> Goodbye World -> 123 -> NULL" / "Hello World -> Goodbye World -> 123 -> nil" / "Hello World -> Goodbye World -> 123 -> nullptr" ( depending on the language ). This also means that the values of each Node must also be non-negative integers so keep that in mind when you are parsing the list from the string.

💡 Example:
>>> linked_list_from_string("1 -> 2 -> 3 -> None")
Node(1, Node(2, Node(3)))
"""

# ✨ Your Solution
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data} -> {self.next}" if self.next else f"{self.data} -> None"

def linked_list_from_string(list_repr: str) -> Node | None:
    list_repr = list_repr.split(" -> ")
    one_word = ["null", "NULL", "nil", "nullptr", "null()", "None", "none"]
    if len(list_repr) <= 1:
        if list_repr[-1] in one_word:
            return None
        else:
            raise ValueError("Str is not available")
    else:
        if list_repr[-1] in one_word:
            list_repr.pop(-1)
        else:
            raise ValueError("There is wrong")
    list_repr = [int(i) for i in list_repr]
    head = Node(list_repr[0])
    current = head
    for i in range(1, len(list_repr)):
        node = Node(list_repr[i])
        current.next = node
        current = node
    return head


# ✅ Test Cases
if __name__ == "__main__":
    print(linked_list_from_string("3 -> 6 -> 9 -> 32 -> 8 -> None"))  # Expected output

# 📝 Note
"""
I'm cooked
"""
