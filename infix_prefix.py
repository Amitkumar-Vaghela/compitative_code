# PART A: infix to postfix conversion



output = []
op = []
priority = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}
exp = input("Enter the infix expression: ")
for ch in exp:
    if ch == '(':
        op.append(ch)
    elif ch == ')':
        while op[-1] != '(':
            ele = op.pop()
            output.append(ele)
        op.pop()
    elif ch in "+-/*^":
        if len(op) > 0:
            while priority[op[-1]] >= priority[ch]:
                ele = op.pop()
                output.append(ele)
                if len(op) == 0:
                    break
        op.append(ch)
    else:
        output.append(ch)

while len(op) != 0:
    ele = op.pop()
    output.append(ele)

print("Infix expression:", exp)
print("Postfix expression:", ''.join(output))





# Part B: Infix to Prefix Conversion
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

output = []
op = []
priority = {
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

exp1 = input("Enter the infix expression: ")
exp = reverse(exp1)

for ch in exp:
    if ch == ')':
        op.append(ch)
    elif ch == '(':
        while op[-1] != ')':
            ele = op.pop()
            output.append(ele)
        op.pop()
    elif ch in "+-/*^":
        if len(op) > 0:
            while priority[op[-1]] >= priority[ch]:
                ele = op.pop()
                output.append(ele)
                if len(op) == 0:
                    break
        op.append(ch)
    else:
        output.append(ch)

while len(op) != 0:
    ele = op.pop()
    output.append(ele)

prefix_expr = reverse(output)
print("Infix expression:", exp1)
print("Prefix expression:", prefix_expr)


