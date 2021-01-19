class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.rt = None

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_leaf(self):
        return not (self.left or self.right)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.prev = None
        self.firmware = None

    def add(self, value):
        if self.root:
            return self.__add(value, self.root)
        self.root = TreeNode(value)
        return self.root

    def __add(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.has_left_child():
                return self.__add(value, curr_node.left)
            curr_node.left = TreeNode(value, parent=curr_node)
            return curr_node.left
        else:
            if curr_node.has_right_child():
                return self.__add(value, curr_node.right)
            curr_node.right = TreeNode(value, parent=curr_node)
            return curr_node.right

    def make_right_sew(self, curr_node):
        if self.prev:
            if not self.prev.right and self.prev != curr_node.parent:
                self.prev.rt = False
                self.prev.right = curr_node
            else:
                self.prev.rt = True
        self.prev = curr_node
        return curr_node

    def get_tree_traversal(self, node):
        while node:
            if self.firmware == "DIRECT":
                print(node.value)
            while node.left:
                node = node.left
                if self.firmware == "DIRECT":
                    print(node.value)
            if self.firmware == "SYMMETRICAL":
                print(node.value)
            while node.right and not node.rt:
                node = node.right
                print(node.value)
            if self.firmware == "DIRECT":
                node = node.left
            else:
                node = node.right

    def make_symmetrical_firmware(self, node):
        if node:
            self.make_symmetrical_firmware(node.left)
            self.make_right_sew(node)
            self.make_symmetrical_firmware(node.right)
        self.firmware = "SYMMETRICAL"

    def make_direct_firmware(self, node):
        if node:
            self.make_right_sew(node)
            self.make_direct_firmware(node.left)
            self.make_direct_firmware(node.right)
        self.firmware = "DIRECT"

    def insert_into_firmware_tree(self, value, curr_node):
        if self.firmware:
            if value < curr_node.value:
                if curr_node.has_left_child():
                    return self.insert_into_firmware_tree(value, curr_node.left)
                if self.firmware == "SYMMETRICAL":
                    curr_node.left = TreeNode(value, parent=curr_node)
                    curr_node.rt = False
                    curr_node.left.right = curr_node
                else:
                    curr_node.left = TreeNode(value, parent=curr_node)
                    curr_node.rt = True
                    curr_node.left.right = curr_node.right
                    curr_node.left.rt = False
                return curr_node.left
            else:
                if curr_node.has_right_child() and curr_node.rt is None:
                    return self.insert_into_firmware_tree(value, curr_node.right)
                if self.firmware == "SYMMETRICAL":
                    temp = curr_node.right
                    curr_node.right = TreeNode(value, parent=curr_node)
                    curr_node.rt = None
                    curr_node.right.right = temp
                    curr_node.right.rt = False
                else:
                    if not curr_node.left:
                        temp = curr_node.right
                        curr_node.right = TreeNode(value, parent=curr_node)
                        curr_node.right.right = temp
                        curr_node.right.rt = False
                    else:
                        curr_node.right = TreeNode(value, parent=curr_node)
                        temp = curr_node.left.right
                        curr_node.left.right = curr_node.right
                        curr_node.right.right = temp
                        curr_node.right.rt = False
                        curr_node.rt = True
                return curr_node.right
        return None

    def find(self, value):
        ptr = self.root
        par = ptr
        while ptr:
            if ptr.value == value:
                return par, ptr
            while ptr.left:
                par = ptr
                ptr = ptr.left
                if ptr.value == value:
                    return par, ptr
            while ptr.right and not ptr.rt:
                par = ptr
                ptr = ptr.right
                if ptr.value == value:
                    return par, ptr
            par = ptr
            ptr = ptr.right

    def delete(self, value):
        find = self.find(value)
        parent_node = find[0]
        curr_node = find[1]
        if curr_node == self.root:
            return
        if curr_node.left:
            if curr_node == parent_node.left:
                parent_node.left = curr_node.left
                curr_node.left.right = curr_node.right
                curr_node.left.rt = True
            else:
                parent_node.right = curr_node.left
                curr_node.left.right = curr_node.right
        elif curr_node.right or curr_node.right is None:
            if parent_node.left == curr_node:
                parent_node.left = curr_node.left
                curr_node.left = curr_node.right
            else:
                parent_node.right = curr_node.right


binary_search_tree = BinaryTree()
