class Node:
    def __init__(self,data):
        self.data=data
        self.next_node=None


class Linked_List:

    def __init__(self):
        self.head = None

    def apppend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node=current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while cu


l_list = Linked_List()
l_list.apppend(1)
l_list.apppend(2)
l_list.apppend(3)
l_list.apppend(4)
print("COMPLETED")