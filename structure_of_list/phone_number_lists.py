import random


class DoubleLinkedNode:
    def __init__(self, phone_number=None, next_element=None,
                 prev_element=None):
        self.number = phone_number
        self.next_element = next_element
        self.prev_element = prev_element


class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, number):
        if self.first is None:
            item = DoubleLinkedNode(number, None, None)
            self.first = item
            self.last = self.first
        else:
            item = DoubleLinkedNode(number, None, self.last)
            self.first.next__item = item
            self.last = item


class SinglyLinkedNode:
    def __init__(self, phone_number=None, next_element=None):
        self.number = phone_number
        self.next_element = next_element


class SinglyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, number):
        if self.first is None:
            self.first = SinglyLinkedNode(number, None)
            self.last = self.first
        else:
            item = SinglyLinkedNode(number, None)
            self.last.next_element = item
            self.last = item

    def sort(self):
        temp = SinglyLinkedNode(None, None)
        item = self.first
        right_item = self.first.next_element
        while item.next_element:
            while right_item:
                if item.number > right_item.number:
                    temp = item.number
                    item.number = right_item.number
                    right_item.number = temp
                right_item = right_item.next_element
            item = item.next_element
            right_item = item.next_element


phone_list = DoubleLinkedList()
for i in range(10):
    if random.randint(0, 1):
        phone_list.add(str(random.randint(1000000, 9999999)))
    else:
        phone_list.add(str(random.randint(100, 999)))

print('All phone numbers:')
phone_list_2 = SinglyLinkedList()
current = phone_list.last
while current:
    print(current.number)
    if len(current.number) == 3:
        phone_list_2.add(current.number)
    current = current.prev_element

phone_list_2.sort()
print('\nSpecial services numbers: ')
current = phone_list_2.first
while current:
    print(current.number)
    current = current.next_element
