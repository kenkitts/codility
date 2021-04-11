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
            print('List is empty')
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value, '=> ', end='')
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

    def reverse(self):
        if not self.head:
            print("There is no head of the list.")
            return
        if self.head.next_node is None:
            print("Only one element in list")
            return

        prev_node = None
        curr_node = self.head
        next_node = self.head.next_node

        while True:
            curr_node.next_node = prev_node
            prev_node = curr_node
            curr_node = next_node
            if next_node is None:
                break
            next_node = next_node.next_node
        self.head = prev_node
        return


ll = LinkedList()

for i in range(0):
    ll.append(i)

ll.print_list()

ll.reverse()

ll.print_list()
