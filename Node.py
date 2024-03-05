
class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None


class Linked_List:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node=current_node.next_node
            current_node.next_node=new_node




linked_list = Linked_List()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
print("Completed")