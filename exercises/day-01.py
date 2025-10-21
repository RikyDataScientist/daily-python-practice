"""
🧠 Challenge: Head, Tail, Init and Last
🔗 Link: https://www.codewars.com/kata/54592a5052756d5c5d0009c3
🏷️ Level: 7 kyu
📅 Date: 2005-10-21

📝 Instruction:
Haskell has some useful functions for dealing with lists:

$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
λ head [1,2,3,4,5]
1
λ tail [1,2,3,4,5]
[2,3,4,5]
λ init [1,2,3,4,5]
[1,2,3,4]
λ last [1,2,3,4,5]
5
Your job is to implement these functions in your given language. Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

head [x] = x
tail [x] = []
init [x] = []
last [x] = x
Here's how I expect the functions to be called in your language:

💡 Example:
>>> head([1,2,3,4,5])
1
>>> tail([1,2,3,4,5])
[2,3,4,5]
"""

# ✨ My Solution
def head(n):
    y = list(n)
    return y[0]
def tail(n):
    y = list(n)
    return y[1:]
def init(n):
    y = list(n)
    return y[:-1]
def last(n):
    y = list(n)
    return y[-1]

# ✅ Test Cases
if __name__ == "__main__":
  print(head([1, 2, 3]))  # 1
  print(tail([1, 2, 3]))  # [2, 3]
  print(init([1, 2, 3]))  # [1, 2]
  print(last([1, 2, 3]))  # 3

# 📝 Note
"""
For 7 kyu, it's so easy for me because for my first try, the code worked.
"""
