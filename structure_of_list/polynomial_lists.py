class Node:
    def __init__(self, rate=None, degree=None, next_element=None):
        self.rate = rate
        self.power = degree
        self.next_element = next_element


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.out = str()

    def __str__(self):
        if self.head is not None:
            current = self.head
            while current:
                self.out += f'{"+" if current.rate >= 0 else "-"}' \
                            f'{current.rate}x^{current.power}'
                current = current.next_element
            return self.out
        return None

    def add(self, rate, degree):
        if self.head is None:
            self.head = Node(rate, degree, None)
            self.last = self.head
        else:
            item = Node(rate, degree, None)
            self.last.next_element = item
            self.last = item

    def clear(self):
        self.__init__()


class Polynomial:
    @staticmethod
    def equality(first_list, second_list):
        current_1 = first_list.head
        current_2 = second_list.head
        while current_1 or current_2:
            if (current_1.rate != current_2.rate or
                    current_1.power != current_2.power):
                return False
            current_1 = current_1.next_element
            current_2 = current_2.next_element
        return True

    @staticmethod
    def add(first_list, second_list, sum_list):
        current_1 = first_list.head
        current_2 = second_list.head
        while current_1:
            sum_list.add(current_1.rate, current_1.power)
            current_1 = current_1.next_element

        current_3 = sum_list.head
        while current_2:
            if current_3.power == current_2.power:
                current_3.rate += current_2.rate
            current_2 = current_2.next_element
            current_3 = current_3.next_element

        return sum_list

    @staticmethod
    def meaning(meaning_list, x):
        current = meaning_list.head
        result = 0
        while current:
            result += current.rate * pow(x, current.power)
            current = current.next_element
        return result


try:
    first_input_list = SinglyLinkedList()
    second_input_list = SinglyLinkedList()
    temp_list = SinglyLinkedList()

    size = int(input('Input max power: '))

    for power in range(size, -1, -1):
        print(f'\nx^{power}' if power else '\nWithout power')
        first_input_list.add(int(input('Input rate for first list: ')), power)
        second_input_list.add(int(input('Input rate for second list: ')), power)
    print(f'\nFirst list: {first_input_list}')
    print(f'Second list: {second_input_list}\n')

    print('Polynomials are equal\n') if Polynomial.equality(
        first_input_list, second_input_list
    ) else print('Polynomials are not equal\n')
    print(
        f'Sum of polynomials: '
        f'{Polynomial.add(first_input_list, second_input_list, temp_list)}'
    )
    print(Polynomial.meaning(
        first_input_list if int(input(
            '\nChoose the meaning list 1 - first, 2 - second: ')
        ) == 1 else second_input_list,
        int(input('Input x: ')))
    )

    first_input_list.clear()
    second_input_list.clear()
except ValueError:
    print('Wrong input!')
