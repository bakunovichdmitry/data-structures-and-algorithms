class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.table = [None] * 7

    def hash_key(self, key):
        return sum([ord(letter) for letter in key]) % len(self.table)

    def resize(self):
        temp_table = self.table
        self.table = [None] * (len(self.table) * 2)
        for item in temp_table:
            curr = item
            while curr:
                self.set(curr.key, curr.value)
                curr = curr.next

    def set(self, key, value):
        if None not in self.table:
            self.resize()
        hash_value = self.hash_key(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = HashNode(key, value)
            return self.table[hash_value]

        curr = self.table[hash_value]
        while True:
            if curr.key == key:
                curr.value = value
                return curr.value
            if curr.next is None:
                break
            curr = curr.next
        curr.next = HashNode(key, value)

    def get(self, key):
        hash_value = self.hash_key(key)
        if not self.table[hash_value]:
            return False
        temp = self.table[hash_value]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return False

    def remove(self, key):
        hash_value = self.hash_key(key)
        if not self.table[hash_value]:
            return False
        else:
            if not self.table[hash_value].next:
                self.table[hash_value] = None
                return
            elif self.table[hash_value].key == key:
                self.table[hash_value] = self.table[hash_value].next
                return
            else:
                curr = self.table[hash_value]
                while curr:
                    if curr.next.key == key:
                        curr.next = curr.next.next
                        return
                    curr = curr.next
                return False

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)


class DictionaryNode:
    def __init__(self, first_letter):
        self.first_letter = first_letter
        self.words = HashTable()
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, first_three_letters):
        if self.head is None:
            self.head = DictionaryNode(first_three_letters)
            self.last = self.head
        else:
            item = DictionaryNode(first_three_letters)
            self.last.next = item
            self.last = item


class Dictionary:
    def __init__(self, _list):
        self.HEAD_LINKED_LIST = _list.head

    def add(self, word, meaning):
        curr = self.HEAD_LINKED_LIST
        while curr:
            if curr.first_letter == word[0].lower():
                curr.words[word] = meaning
                return f'Word "{word}" added in dictionary'
            curr = curr.next

    def get(self, word):
        curr = self.HEAD_LINKED_LIST
        while curr:
            if curr.first_letter == word[0].lower():
                return curr.words[word]
            curr = curr.next

    def delete(self, word):
        curr = self.HEAD_LINKED_LIST
        while curr:
            if curr.first_letter == word[0].lower():
                del curr.words[word]
                return f'Word "{word}" removed from dictionary'
            curr = curr.next


linked_list = LinkedList()

linked_list.add('a')
linked_list.add('b')
linked_list.add('c')

_dict = Dictionary(linked_list)

if __name__ == '__main__':
    keys = [
        'a', 'ab', 'ac', 'ad', 'abc', 'a',
        'b', 'bb', 'bc', 'ba', 'b', 'boa',
        'c', 'ca', 'cv', 'cy', 'caq', 'asd',
    ]
    values = [
        'q', 'w', 'e', 'r', 't', 'y',
        'u', 'i', 'o', 'p', 'a', 's',
        'd', 'f', 'g', 'h', 'j', 'k',
    ]

    for i in range(len(keys)):
        _dict.add(keys[i], values[i])

    for i in range(len(keys)):
        print(keys[i], _dict.get(keys[i]))

    for i in range(len(keys)):
        _dict.delete(keys[i])

    for i in range(len(keys)):
        print(keys[i], _dict.get(keys[i]))
