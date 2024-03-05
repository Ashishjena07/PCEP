class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class Linked_List:

    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node=current_node.next_node
            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node.next_node:
            print(current_node.data," -> ", end="")
            current_node = current_node.next_node
        print(current_node.data)


l_list = Linked_List()
l_list.append(1)
l_list.append(2)
l_list.append(3)
l_list.append(4)
l_list.display()
print("Completed")