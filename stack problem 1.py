def is_balanced(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        # Push opening brackets onto the stack
        if ch in "({[":
            stack.append(ch)

        # Check closing brackets
        elif ch in ")}]":
            # Stack empty means no matching opening bracket
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    # Balanced only if all opening brackets were matched and popped
    return len(stack) == 0


s = "({[]})"
print("Is Balanced:", is_balanced(s))