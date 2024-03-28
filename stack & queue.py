class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class Queue:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node.next_node:
            print(current_node.data, " -> ", end="")
            current_node = current_node.next_node
        print(current_node.data)

    def pop(self):
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next_node
            return popped_node.data

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next_node
            return popped_node.data

    def display(self):
        current_node = self.top
        while current_node:
            print(current_node.data, " -> ", end="")
            current_node = current_node.next_node
        print()

# Example usage
l_list = Queue()
l_list.append(1)
l_list.append(2)
l_list.append(3)
l_list.append(4)
l_list.display()
l_list.pop()
l_list.pop()
l_list.display()
print("Queue operations completed")

s_stack = Stack()
s_stack.push(1)
s_stack.push(2)
s_stack.push(3)
s_stack.push(4)
s_stack.display()
s_stack.pop()
s_stack.pop()
s_stack.display()
print("Stack operations completed")