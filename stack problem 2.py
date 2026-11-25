def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            # Pop the right operand first, then the left operand
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                # Truncate toward zero (standard in RPN problems like LeetCode)
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print("RPN Result:", eval_rpn(tokens))