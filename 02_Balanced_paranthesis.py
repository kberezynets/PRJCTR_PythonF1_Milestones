# Balanced parenthesis
# Write a function `is_balanced`  that takes in a string of symbols '(' and ')'
# and tells whether it is balanced. Examples:
# - `is_balanced('()') -> True`
# - `is_balanced('())') -> False`
# - `is_balanced('(()') -> False`
# - `is_balanced(')())') -> False`

def is_balanced(a: str):
    res = False
    if len(a) % 2 == 0:
        res = True
        for i in range(0, int(len(a)/2)):
            if a[i] == '(' and a[-i-1] == '(' or a[i] == ')' and a[-i-1] == ')':
                res = False
                break
    print(res)


is_balanced('()')
is_balanced('())')
is_balanced('(()')
is_balanced(')())')
