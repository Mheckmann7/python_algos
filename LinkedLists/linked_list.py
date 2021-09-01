class node: 
    def __init__(self, data = None): 
        self.data = data # pass in element to be stored by the structure, stores last data point
        self.next = None # last element will always have its last element set = to none

class lined_list:
    def __init__(self):
        self.head = node() # user can't access it, only points to first element in list

    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.head != None: 
            current = current.next
        current.next = new_node # once we get to the end of the linked list add the new node
    
    def length(self):
        current = self.head
        total = 0 
        while current.next != None:
            total += 1
            current = current.next
        return total 

    def display(self): 
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
