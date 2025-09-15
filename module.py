
class Array:
    def __init__(self):
        self.value = []

    def append(self, item):
        self.value += [item] 

    def pop(self, index =-1):
        if index < 0:
            index += len(self.value)
        if index < 0 or index >= len(self.value):
            raise IndexError("index out of range") 
        else:   
            item = self.value[index]
            self.value = self.value[:index] + self.value[index +1:]
            return item
    
    def insert(self, index, item):       
        if index > len(self.value):
            index = len(self.value)
        self.value = self.value[:index] + [item] + self.value[index:]          
    
    def remove(self, item):
       for i in range(len(self.value)):
           if self.value[i] == item:
               self.value.pop(i)
               return self.value
