class Stack:

    def __init__(self):
        self.stack = []
    
    def insert(self, x):
        self.stack.append(x)
    
    def remove(self):
        if(self.stack != []):
            self.stack.pop(len(self.stack) - 1)

    def length(self):
        return(print(len(self.stack)))
    
    def empty(self):
        if(self.stack == []):
            print('Vazio')
        print('Não Vazio')

    def head(self):
        return print(self.stack[-1])
