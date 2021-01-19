class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_leaf(self):
        return not (self.left or self.right)

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left
        return current

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.parent and self.parent.left == self:
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def cut(self):
        if self.parent.left == self:
            self.parent.left = self.right
            if self.right is not None:
                self.right.parent = self.parent
        else:
            self.parent.right = self.left
            if self.left is not None:
                self.right.parent = self.parent


class BinaryTree:
    def __init__(self):
        self.root = None

    def __getitem__(self, value):
        return self.get(value)

    def __delitem__(self, value):
        self.delete(value)

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

    def get(self, value):
        if self.root:
            result = self.__get(value, self.root)
            if result:
                return result
            return False
        else:
            return False

    def __get(self, value, curr_node):
        if not curr_node:
            return None
        elif curr_node.value == value:
            return curr_node
        elif value < curr_node.value:
            return self.__get(value, curr_node.left)
        else:
            return self.__get(value, curr_node.right)

    def delete(self, value):
        if self.root:
            root_node = self.root
            is_root_node_has_child = (
                root_node.has_left_child() or root_node.has_right_child()
            )
            if is_root_node_has_child:
                remove_node = self.__get(value, self.root)
                if remove_node:
                    return self.__delete(remove_node)
                return None
            elif not is_root_node_has_child and self.root.value == value:
                self.root = None
            else:
                return None

    def __delete(self, remove_node):
        parent_node = remove_node.parent
        # If remove node is leaf
        if remove_node.is_leaf():
            if remove_node == remove_node.parent.left:
                parent_node.left = None
            else:
                parent_node.right = None

        # If remove node has one child
        elif not remove_node.left or not remove_node.right:
            if not remove_node.has_left_child():
                if parent_node.left == remove_node:
                    parent_node.left = remove_node.right
                else:
                    parent_node.right = remove_node.right
                remove_node.right.parent = parent_node
            else:
                if parent_node.left == remove_node:
                    parent_node.left = remove_node.left
                else:
                    parent_node.right = remove_node.left
                remove_node.left.parent = parent_node

        # If remove node has two child
        else:
            successor = remove_node.find_successor()
            successor.cut()
            remove_node.value = successor.value

    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)


binary_search_tree = BinaryTree()
