class Stack:

    def __init__(self, items = [], limit = 100):
        self.items= [1,2,3,4,5]
        



    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
       

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self, item):
        if len(self.items) < self.capacity:
             self.items.append(item)
        else:
            print('cannot push')
    def search(self, target):
         for index, item in enumerate(self.items[::-1], 1):
            if item == target:
                return index
         return -1
