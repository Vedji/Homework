# by Veji

class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val is not None and isinstance(val, (str, list)) and ('(' in val or ')' in val):
            val = val[1:] if val[0] == '(' else val
            val = val[:len(val) - 1] if val[len(val)-1] == ')' else val
        if isinstance(val, list) and len(val) == 1:
            val = val[0]
        self._value = val


def check_sequence(sequence: str) -> bool:
    """ Проверяет правильность скобочной последовательности. """
    error_flag = False
    commands_stack = {')': '(', '}': '{', ']': '['}
    stack = []
    for symbol in sequence:
        if symbol in commands_stack.values():
            stack.append(symbol)
        elif symbol in commands_stack:
            if len(stack) != 0:
                c = stack.pop()
                if commands_stack[symbol] != c:
                    error_flag = True
                    break
            else:
                error_flag = True
    return error_flag


def minimum_priority(expression: list) -> int:
    min_priority = 100
    position = -1
    brackets = 0
    priority = {}

    def priority_symbol(sim: str) -> int:
        priority_sym = min_priority + 1
        priority_sym = 1 if sim in '+-' else priority_sym
        priority_sym = 2 if sim in '*/' else priority_sym
        return priority_sym

    for i in range(len(expression)):
        brackets += 1 if expression[i] == '(' else 0
        brackets -= 1 if expression[i] == ')' else 0
        if expression[i] in '+-*/':
            if brackets not in priority:
                priority[brackets] = [i]
            else:
                priority[brackets] += [i]

    if priority != {}:
        for i in priority[min(priority)]:
            if priority_symbol(expression[i]) <= min_priority:
                min_priority = priority_symbol(expression[i])
                position = i

    return position


def make_tree(value) -> Node:

    k = minimum_priority(value)
    if k < 0:  # создать лист
        tree = Node(value)
    else:  # создать узел-операцию
        tree = Node(value[k])
        tree.left = make_tree(value[:k])
        tree.right = make_tree(value[k+1:])
    return tree


def computation_tree(tree: Node):
    if tree.left is None:
        return float(tree.value)
    else:
        n1 = computation_tree(tree.left)
        n2 = computation_tree(tree.right)

        if tree.value == "+":
            res = n1 + n2
        elif tree.value == "-":
            res = n1 - n2
        elif tree.value == "*":
            res = n1 * n2
        else:
            res = n1 / n2
        return res


input_data = '(10 - (4 * 2) - 1) * (20 * 2) / 8'


if check_sequence(input_data):
    print('Ошибка в скобочной последовательности')
else:
    arr = []
    buff = ''
    for i in input_data:
        if i in '0123456789.':
            buff += i
        elif i in '()+-*/':
            if buff:
                arr.append(buff)
                buff = ''
            arr.append(i)
    if buff != '' and buff in '0123456789':
        arr.append(buff)
    tr = make_tree(arr)
    print(computation_tree(tr))
