"""
Use a stack to check whether or not a string has
balanced usage of parenthesis.

Examples:
    (), ()(), (({{[]}})) <- balanced
    ((), {{{}}], [][]]] <- unbalanced

Use cases:
balanced -> [{()}]

unbalanced -> (()
unbalanced -> ))

"""

from stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_parenthesis_balanced(parenthesis_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parenthesis_string) and is_balanced:
        parenthesis = parenthesis_string[index]
        if parenthesis in "{([":
            s.push(parenthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parenthesis):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

#Used Test Cases
print(is_parenthesis_balanced("(({{[]}}))"))
print(is_parenthesis_balanced("({[]}})"))
print(is_parenthesis_balanced("(({{[}}))"))
print(is_parenthesis_balanced("(({{}}))"))
print(is_parenthesis_balanced("(({{[]}})"))
print(is_parenthesis_balanced("))"))
