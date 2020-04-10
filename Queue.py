class Queue:

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def remove(self):
        if(self.queue != []):
            self.queue.pop(0)
    
    def empty(self):
        if(self.queue == []):
            return print('Empty')
        return print('Not empty')
    
    def first(self):
        if(self.queue != []):
            return print(self.queue[0])
    
    def last(self):
        if(self.queue != []):
            return print(self.queue[len(self.queue) - 1])

    def length(self):
        return print(len(self.queue))

    def show(self):
        for i in self.queue:
            print(i, end = ' ')

q = Queue()
q.empty()
q.push(2)
q.push(3)
q.push(7)
q.show()
q.length()
q.empty()
q.first()
q.last()
q.remove()
q.first()
q.remove()
q.first()
q.length()
q.show()
