class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def getLabel(self):
        return (self.value)

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def insert(self, value, index):
        if index >= 0:
            node = Node(value)
            if(self.empty()):
                self.first = node
                self.last = node
            else:
                if(index == 0):
                    node.setNext(self.first)
                    self.first = node
                elif(index >= self.len_list):
                    self.last.setNext(node)
                    self.last = node
                else:
                    present_node = self.first
                    next_node = self.first.getNext()
                    present_index = 1

                    while next_node != None:

                        if(present_index == index):
                            node.setNext(next_node)
                            present_node.setNext(node)
                        
                        present_node = next_node
                        next_node = next_node.getNext()
                        present_index += 1
        
        self.len_list += 1
    
    def remove(self, index):
        if(self.empty() == False and index >= 0 and index < self.len_list):

            aux_remove = False

            if(self.first.getNext() == None):
                self.first = None
                self.last = None
                aux_remove = True
            elif(index == 0):
                self.first = self.first.getNext()
                aux_remove = True
            else:
                present_node = self.first
                next_node = self.first.getNext()
                present_index = 1

                while next_node != None:

                    if(present_index == index):
                        present_node.setNext(next_node.getNext())
                        next_node.setNext(None)
                        aux_remove = True
                    
                    present_node = next_node
                    next_node = next_node.getNext()
                    present_index += 1
        
        if(aux_remove):
            self.len_list -= 1 
    
    def empty(self):
        if(self.first == None):
            return True
        return False
    
    def length(self):
        return self.len_list

    def show(self):
        next_node = self.first

        while next_node != None:
            print(next_node.getLabel(), end = ' ')
            next_node = next_node.getNext()
        print(' ')
        