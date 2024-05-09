def isValid(S: str) -> bool:
    stk = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in S:
        if char in mapping.values():
            stk.append(char)
            print(f"Pushed {char} onto stack: {stk}")
        elif char in mapping:
            if not stk or stk.pop()!= mapping[char]:
                return False
            print(f"Popped {char} from stack: {stk}")

    return not stk

S = "(])"
print(isValid(S)) 