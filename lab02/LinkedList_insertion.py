def insert_sort_linkedlist(a):
    if a is None or len(a) <= 1:
        return
    else:
        node_i = a.head.next.next  # node at position 1
        node_i_pre = a.head.next
        i = 1
        while i < len(a):
            node_j_pre = a.head
            node_j = a.head.next
            j = 0
            while j < i and node_j.data <= node_i.data:
                j += 1
                node_j_pre = node_j
                node_j = node_j.next
            if i != j:
                node_i_pre.next = node_i.next
                node_j_pre.next = node_i
                node_i.next = node_j
                node_i = node_i_pre.next
            else:
                node_i_pre = node_i
                node_i = node_i.next
            print(a)
            i += 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, a=None):
        self.head = Node(None)  # a dummy head node
        if a:
            for data in a:
                self.insert(data, pos=len(self))

    def __len__(self):
        cur_node = self.head.next
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    def __repr__(self):
        rep = ''
        cur_node = self.head.next
        while cur_node:
            rep += str(cur_node) + ', '
            cur_node = cur_node.next
        if len(rep) > 0:
            rep = rep[:-2]
        return '[' + rep + ']'

    def locate(self, pos):
        if pos < 0 and pos >= len(self):
            print('Index out of range!')
            return None
        count = 0
        pre_node = self.head
        cur_node = pre_node.next
        while cur_node and count < pos:
            pre_node = cur_node
            cur_node = cur_node.next
            count += 1
        return pre_node, cur_node

    def insert(self, data, pos=0):
        if pos < 0 or pos > len(self):  # n + 1 possible insertion position
            print('Index out of range!')
            return
        new_node = Node(data)
        pre_node, cur_node = self.locate(pos)
        pre_node.next = new_node
        new_node.next = cur_node

    def delete(self, pos):
        if pos < 0 or pos >= len(self):  # n possible deletion position
            print('Index out of range!')
            return
        pre_node, cur_node = self.locate(pos)
        pre_node.next = cur_node.next
        del (cur_node)