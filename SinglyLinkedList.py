class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def find(root: Node, val) -> int:
    i = 0
    curr = root
    while curr:
        if curr.data == val:
            return i
        curr = curr.next
        i += 1
    return -1


def insert_at_start(root: Node, val) -> Node:
    node = Node(val)
    node.next = root
    return node


def insert_at_end(root: Node, val) -> Node:
    node = Node(val)
    curr = root
    while curr.next:
        curr = curr.next
    curr.next = node
    return root


def insert_at_pos(root: Node, val, pos: int) -> Node:
    node = Node(val)
    if not root:
        return node
    if not pos:
        return insert_at_start(root, val)
    curr = root
    prev = None
    i = 0
    while curr.next and i < pos:
        prev = curr
        curr = curr.next
        i += 1
    if i < pos:
        raise ValueError("Index is greater than length")
    if not curr.next:
        return insert_at_end(root, val)
    node.next = curr
    prev.next = node
    return root


def _print(root: Node):
    ans = []
    while root:
        ans.append(root.data)
        root = root.next
    print(" -> ".join([str(elem) for elem in ans]))


def delete_from_start(root: Node) -> Node:
    return root.next


def delete_from_end(root: Node) -> Node:
    curr = root
    while curr.next:
        curr = curr.next
    curr.next = None
    return root


def delete_from_pos(root: Node, pos: int) -> Node:
    if not root.next:
        return delete_from_start(root)
    i = 0
    curr = root
    prev = None
    while curr.next and i < pos:
        prev = curr
        curr = curr.next
        i += 1
    if i < pos:
        raise ValueError("Index is greater than length")
    if not curr.next:
        return delete_from_end(root)
    prev.next = curr.next
    return root


def reverse(root: Node) -> Node:
    curr = root
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def get_nth_node_from_end_val(root: Node, n: int):
    ptr_1 = root
    idx = 0
    while ptr_1 and idx < n:
        ptr_1 = ptr_1.next
        idx += 1
    if idx < n or not ptr_1:
        return None
    ptr_2 = root
    while ptr_1.next:
        ptr_1 = ptr_1.next
        ptr_2 = ptr_2.next
    return ptr_2.data


def check_cycle(root: Node) -> bool:
    ptr_fast = root
    ptr_slow = root
    while ptr_fast and ptr_slow:
        ptr_fast = ptr_fast.next
        if not ptr_fast:
            return False
        if ptr_fast == ptr_slow:
            return True
        ptr_fast = ptr_fast.next
        if ptr_fast == ptr_slow:
            return True
        ptr_slow = ptr_slow.next


def return_ptrs_if_cycle(root: Node) -> (Node, Node):
    if not root or not root.next:
        return None, None
    ptr_slow = root.next
    ptr_fast = ptr_slow.next
    while ptr_slow != ptr_fast:
        ptr_slow = ptr_slow.next
        try:
            ptr_fast = ptr_fast.next.next
        except AttributeError:  # ptr_fast = None implies no cycle
            return None, None
    return ptr_fast, ptr_slow


def detect_cycle_start_node(root: Node) -> Node:
    ptr_fast, ptr_slow = return_ptrs_if_cycle(root)
    if not ptr_fast or not ptr_slow:
        return None
    ptr_slow = root  # there is a cycle => get slow back to the root and walk both ptrs one at a time
    while ptr_slow != ptr_fast:
        ptr_slow = ptr_slow.next
        ptr_fast = ptr_fast.next
    return ptr_slow


def detect_cycle_length(root: Node) -> int:
    ptr_slow, ptr_fast = return_ptrs_if_cycle(root)
    if not ptr_fast or not ptr_slow:
        return 0
    loop_len = 0
    ptr_slow = ptr_slow.next
    while ptr_slow != ptr_fast:
        ptr_slow = ptr_slow.next
        loop_len += 1
    return loop_len


def get_intersection_node(l1: Node, l2: Node) -> Node:
    curr1, curr2 = l1, l2
    i1, i2 = 0, 0
    while curr1:
        curr1 = curr1.next
        i1 += 1
    while curr2:
        curr2 = curr2.next
        i2 += 1
    curr1, curr2 = l1, l2
    if i1 > i2:
        for i in range(i1 - i2):
            curr1 = curr1.next
    elif i2 > i1:
        for i in range(i2 - i1):
            curr2 = curr2.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1


def get_middle_node(root: Node) -> Node:
    ptr_slow = root
    ptr_fast = root
    while ptr_fast:
        ptr_fast = ptr_fast.next
        if not ptr_fast:
            return ptr_slow
        ptr_slow = ptr_slow.next
        ptr_fast = ptr_fast.next
    return ptr_slow


def merge_two_sorted_list(l1: Node, l2: Node) -> Node:
    if l1.data < l2.data:
        temp = Node(l1.data)
        l1 = l1.next
    else:
        temp = Node(l2.data)
        l2 = l2.next
    curr = temp
    while l1 and l2:
        if l1.data < l2.data:
            curr = Node(l1.data)
            l1 = l1.next
        else:
            curr = Node(l2.data)
            l2 = l2.next
    if not l1:
        curr.next = l2
    else:
        curr.next = l1
    return temp


def _swap_data(a: Node, b: Node):
    temp = a.data
    a.data = b.data
    b.data = temp


def reverse_in_pairs(root: Node) -> Node:
    temp = root
    while temp and temp.next:
        _swap_data(temp, temp.next)
        temp = temp.next.next
    return root


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    n1 = insert_at_start(n1, 0)
    n1 = insert_at_end(n1, 6)
    n1 = insert_at_pos(n1, 0, 3)
    print(f"Elem at position 1: {find(n1, 1)}")  # Expected = 1
    print("List before deleting: ")
    _print(n1)  # Expected = 0 -> 1 -> 2 -> 0 -> 3 -> 4 -> 5 -> 6
    n1 = delete_from_pos(n1, 3)
    print("List after deleting from position 3: ")
    _print(n1)  # Expected = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    print(f"3rd node from end: {get_nth_node_from_end_val(n1, 3)}")
    print(f"Loop length: {detect_cycle_length(n1)}")
    rev = reverse(n1)
    print("List after reversal: ")
    _print(rev)  # Expected = 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0
