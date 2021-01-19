class StackNode:
    def __init__(self, sign, next_element=None):
        self.sin = sign
        self.next = next_element


class Stack:
    OPERATION_PRIORITIES = {
        '(': 0,
        ')': 1,
        '+': 2, '-': 2,
        '*': 3, '/': 3,
        '^': 4,
    }

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, sign):
        if self.head is None:
            self.head = StackNode(sign, None)
            self.tail = self.head
        else:
            item = StackNode(sign, self.head)
            self.head = item

    def pop(self):
        if self.head is None:
            return None
        item = self.head
        self.head = self.head.next
        return item

    def is_empty(self):
        return False if self.head else True

    def get_postfix_record(self, infix_record):
        out_record = []

        for item in infix_record:
            if item in self.OPERATION_PRIORITIES:
                if self.is_empty():
                    self.push(item)
                else:
                    if item == ')':
                        while True:
                            stack_item = self.pop()
                            stack_sign = stack_item.sign
                            if stack_sign == '(':
                                break
                            out_record.append(stack_sign)
                    elif item == '(':
                        self.push(item)
                    else:
                        while not self.is_empty():
                            stack_item = self.pop()
                            stack_sign = stack_item.sign
                            if (self.OPERATION_PRIORITIES[item] >
                                    self.OPERATION_PRIORITIES[stack_sign]):
                                self.push(stack_sign)
                                break
                            out_record.append(stack_sign)
                        self.push(item)
            else:
                out_record.append(item)

        # Retrieving remaining items on the stack
        while not self.is_empty():
            item = self.pop()
            out_record.append(item.sign)
        return ''.join(out_record)

    def get_prefix_record(self, infix_record):
        inverted_record = ''
        for i in reversed(infix_record):
            if i == '(':
                inverted_record += ')'
            elif i == ')':
                inverted_record += '('
            else:
                inverted_record += i
        return ''.join(reversed(self.get_postfix_record(inverted_record)))


_stack = Stack()
print(_stack.get_postfix_record('A+B*C-D/(A+B)'))
print(_stack.get_prefix_record('A+B/(C-D)'))
