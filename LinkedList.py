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
        while curr_node:
            next_node = curr_node.next_node
            curr_node.next_node = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        return

    def delete_list(self):
        if self.head is None:  # If no head to list, exit
            print('No elements in list, nothing to delete.')
            return False

        if self.head.next_node is None:  # If only one elements in list, delete and exit
            del self.head
            self.head = None
            return True

        curr_node = self.head
        while curr_node:
            next_node = curr_node.next_node
            curr_node.next_node = None
            del curr_node
            curr_node = next_node

        self.head = None
        return True

    def delete_item(self, value):
        if self.head is None:
            print('List empty, nothing to delete.')
            return False

        elif self.head.value == value:
            self.head = self.head.next_node
            return True

        curr_node = self.head
        prev_node = curr_node
        while curr_node and curr_node.value != value:
            prev_node = curr_node
            curr_node = curr_node.next_node
        if not curr_node:
            return False
        prev_node.next_node = curr_node.next_node
        curr_node.next_node = None

        return True

    def insert(self, value, insertion_point):
        node = Node(value)
        if self.head is None:
            return False

        curr_node = self.head
        while curr_node and curr_node.value != insertion_point:
            curr_node = curr_node.next_node
        if curr_node is None:
            return False
        if curr_node.value == insertion_point:
            node.next_node = curr_node.next_node
            curr_node.next_node = node



ll = LinkedList()

for i in range(10):
    ll.append(i)

ll.print_list()

ll.insert('X', )

ll.print_list()