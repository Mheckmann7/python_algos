class Node: 
    def __init__(self, data = None, next  = None): 
        self.data = data # pass in element to be stored by the structure, stores last data point
        self.next = next # pointer to the next element
        # last element will always have its last element set = to none

class linked_list:
    def __init__(self):
        self.head = None # user can't access it, only points to first element in list

    def insert_at_begining(self, data):
        node = Node(data, self.head) # will create the new node and set the pointer = to the current head
        self.head = node # make node the new head 

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iterator = self.head
        linked_list_str = ''
        while iterator:
            linked_list_str += str(iterator.data) 
            iterator = iterator.next

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) # if list is blank set the head equal to the node created with that data
            return
        iterator = self.head
        while iterator.next: # if iterator.next has some value we are not at the end 
            iterator = iterator.next
        iterator.next = Node(data, None) #we have reached the end so set the itr.next = to the new node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list: 
            self.insert_at_end(data)


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


    def get(self,index):
        if index >= self.length():
            print('Error')
            return None
        current_idx = 0
        current_node = self.head
        while True: # dont have to worry about forever loop bc we checked that the index is not longer than the length of the list 
            current_node = current_node.next
            if current_idx == index: 
                return current_node.data
            current_idx += 1 

    def delete(self, index):
        if index >= self.length():
            return
        current_idx = 0
        current_node = self.head
        while True:
            last_node = current_node #make sure we keep track of the node before the one we erase
            current_node = current_node.next
            if current_idx == index:
                last_node.next = current_node.next # skip past the current node to erase it
                return 
            current_idx += 1 # if we aren't at the current index continue down list