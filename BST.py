from time import perf_counter
import random

class BST():
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self,value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BST(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BST(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def find(self, value):
        if self.value is None:
            return False
        elif value < self.value:
            if self.left is None:
                return str(value) + " Not Found"
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return str(value) + " Not Found"
            else:
                return self.right.find(value)
        else:
            return str(value) + " Found"

    def print(self):
        if self.left:
            self.left.print()
        print(self.value)
        if self.right:
            self.right.print()

    def delete(self, value):
        if self.value == value:





bst = BST()

for x in range(0,100):
    bst.insert(random.randint(0,10))

bst.print()
