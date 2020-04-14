class Deque:

    def __init__(self):
        self.deque = []

    def inserir_front(self, x):
        self.deque.insert(0, x)
    
    def remove_front(self):
        if(self.deque != []):
            self.deque.pop(0)
    
    def inserir_back(self, x):
        self.deque.append(x)

    def remove_back(self):
        if(self.deque != []):
            self.deque.pop(len(self.deque) - 1)
    
    def front(self):
        return print(self.deque[0])

    def back(self):
        return print(self.deque[-1])
    
    def vazio(self):
        if(self.deque == []):
            return print('Vazio')
        return print('Não vazio')

    def imprime(self):
        for i in self.deque:
            print(i, end = ' ')
