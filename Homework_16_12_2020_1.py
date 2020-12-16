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
        v = val
        if val is not None:
            for y in val:
                for x in '0123456789+-*/.':
                    if x in y:
                        v = y
        self._value = v


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

    for p in range(len(expression)):
        brackets += 1 if expression[p] == '(' else 0
        brackets -= 1 if expression[p] == ')' else 0
        if expression[p] in '+-*/':
            if brackets not in priority:
                priority[brackets] = [p]
            else:
                priority[brackets] += [p]

    if priority != {}:
        for br in priority[min(priority)]:
            if priority_symbol(expression[br]) <= min_priority:
                min_priority = priority_symbol(expression[br])
                position = br

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


def computation_tree(tree: Node) -> float:
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


# input_data = '((((2+2)*2) - 2) * (10 * 5 - 8 * 9)) / 2 + (6 - 40)'  # == -100
input_data = input('Введите выражение: ')


if check_sequence(input_data):
    print('Ошибка в скобочной последовательности')
else:
    arr = []
    last_sign = False
    buff = ''
    for i in input_data:
        if i in '0123456789.' or (i == '-' and last_sign):
            buff += i
            last_sign = False
        elif i in '()+-*/':
            if i in '(+-*/':
                last_sign = True
            if buff:
                arr.append(buff)
                buff = ''
            arr.append(i)
    if buff != '':
        for i in '01234567890-.':
            if i in buff:
                arr.append(buff)
                break
    print(computation_tree(make_tree(arr)))
