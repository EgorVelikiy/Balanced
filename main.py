class Stack():

    def __init__(self, stack: str = ''):
        self.stack = list(stack)

    def is_empty(self):
        return False if len(self.stack) > 0 else True

    def push(self, item: str):
        self.stack += item

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


pair = ['()', '{}', '[]']


def balanced(stack):
    if stack.is_empty() or stack.size() % 2 != 0:
        return 'Несбалансированно'
    else:
        counter_1 = 0
        counter_2 = 0
        counter_3 = 0
        for brack_1 in stack.stack:
            if brack_1 == '(':
                counter_1 += 1
            elif brack_1 == ')':
                counter_1 -= 1

        if counter_1 != 0:
            return "Небалансированно"

        for brack_2 in stack.stack:
            if brack_2 == '[':
                counter_2 += 1
            elif brack_2 == ']':
                counter_2 -= 1

        if counter_2 != 0:
            return "Небалансированно"

        for brack_3 in stack.stack:
            if brack_3 == '{':
                counter_3 += 1
            elif brack_3 == '}':
                counter_3 -= 1

        if counter_3 != 0:
            return "Небалансированно"

    return "Сбалансированно"


def test():
    stack = Stack('(((([{}]))))')
    print(balanced(stack))
    stack = Stack('[([])((([[[]]])))]{()}')
    print(balanced(stack))
    stack = Stack('{{[()]}}')
    print(balanced(stack))
    stack = Stack('}{}')
    print(balanced(stack))
    stack = Stack('{{[(])]}}')
    print(balanced(stack))
    stack = Stack('[[{())}]')
    print(balanced(stack))
    stack = Stack('[]{}[]((((((((()))')
    print(balanced(stack))
    stack = Stack('')
    print(balanced(stack))
    stack = Stack('((([{}]{})))')
    print(balanced(stack))


if __name__ == '__main__':
    test()
