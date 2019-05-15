"""
Use a stack data structure to convert number to it's binary value.

Method:
    Divide by two Method
Example:
    202%2 = 101 -> 0
    101%2 = 50  -> 1
    50%2  = 25  -> 0
    25%2  = 12  -> 1
    12%2  = 6   -> 0
    6%2   = 3   -> 0
    3%2   = 1   -> 1
    1%2   = 0   -> 1

    202 = 11001010
"""

from stack import Stack


def convertToBinary(num):
    s = Stack()
    while num > 0:
        rem = num % 2
        s.push(rem)
        num = num // 2
    # print(s.get_stack())

    binary_num = ""
    while not s.is_empty():
        binary_num += str(s.pop())
    # print(s.get_stack())
    return binary_num


print(convertToBinary(482))
