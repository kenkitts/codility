class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                break
            current_node = current_node.next_node

    def print_list(self):
        if self.head is None:
            print('None')
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value, '=>')
            current_node = current_node.next_node
        print('None')
        return

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        node.next_node = self.head
        self.head = node


