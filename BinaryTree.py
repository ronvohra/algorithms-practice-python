from queue import Queue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def inorder(node, result):
    if not node:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


def preorder(node, result):
    if not node:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)


def postorder(node, result):
    if not node:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)


def level_order(node, result):
    if not node:
        return
    q = Queue()
    q.put(node)
    while not q.empty():
        temp_node = q.get()
        result.append(temp_node.data)
        if temp_node.left:
            q.put(temp_node.left)
        if temp_node.right:
            q.put(temp_node.right)


def reverse_level_order(node):
    if not node:
        return False
    q = Queue()
    s = []
    q.put(node)
    while not q.empty():
        temp_node = q.get()
        if temp_node.left:
            q.put(temp_node.left)
        if temp_node.right:
            q.put(temp_node.right)
        s.insert(0, temp_node)
    while len(s) > 0:
        print(s.pop(0).data)


def find_max_node(node):
    max_data = float("-infinity")
    if not node:
        return max_data
    if node.data > max_data:
        max_data = node.data
    find_max_node(node.left)
    find_max_node(node.right)
    return max_data


def find(node, val):
    if not node:
        return False
    if node.data == val:
        return True
    else:
        temp = find(node.left, val)
        if temp:
            return temp
        else:
            return find(node.right, val)


def find_size(node):
    if not node:
        return 0
    return find_size(node.left) + find_size(node.right) + 1


def find_depth(node):
    if not node:
        return 0
    return max(find_depth(node.left), find_depth(node.right)) + 1


def find_deepest_node(node):
    if not node:
        return
    q = Queue()
    q.put(node)
    temp_node = None
    while not q.empty():
        temp_node = q.get()
        if temp_node.left:
            q.put(temp_node.left)
        if temp_node.right:
            q.put(temp_node.right)
    return temp_node.data


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n1.left(n2)
    n1.right(n3)
    n1.right.left(n4)
    n1.right.right(n5)
    n1.left.left(n6)
    n1.left.right(n7)
