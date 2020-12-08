# by Veji


def check_sequence(sequence: str) -> bool:
    error_flag = True
    commands_stack = {')': '(', '}': '{', ']': '['}
    stack = []
    for symbol in sequence:
        if symbol in commands_stack.values():
            stack.append(symbol)
        elif symbol in commands_stack:
            c = stack.pop()
            if commands_stack[symbol] != c:
                error_flag = False
                break
    return error_flag


input_sequence = '()[{()[]}]'  # правильная
print(check_sequence(input_sequence))   # True

input_sequence = '({[)}]'  # неправильная
print(check_sequence(input_sequence))   # False
