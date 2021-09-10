class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None # initialize a linked list

    #print out linked list
    def print_list(self):
        cur_node = self.head # start at the head of the list
        while cur_node:
            print(cur_node.data) # print out the data
            cur_node = cur_node.next

    # add a node to the end of the linked list
    def append(self, data):
        new_node = Node(data) # create a new node
        if self.head is None: # means there is no node in the list
            self.head = new_node # set the head to the new node
        last_node = self.head # starts at begining of list
        while last_node.next: #while last node is not None
            last_node = last_node.next # move the head pointer to the right
        last_node.next = new_node # set the new node to the end of the list

    # add node to the begining of the list 
    def prepend(self, data):
        new_node = Node(data) 
        new_node.next = self.head # point new node to the head of the list
        self.head = new_node # make the new node the head of the list

    # insert after a given node
    def insert_after_node(self, prev_node, data): # takes node to insert after
        if not prev_node: 
            return # previous node is not in the list
        new_node = Node(data)
        new_node.next = prev_node.next # new node.next points to previous node.next
        prev_node.next = new_node # make the previous node point to the new node


