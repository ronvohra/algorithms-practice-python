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
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)


def find_max(node):
    max_data = float("-infinity")
    if not node:
        return max_data
    if node.data > max_data:
        max_data = node.data
    find_max(node.left)
    find_max(node.right)
    return max_data


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
