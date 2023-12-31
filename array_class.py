class Array:
    
    def __init__(self):
        self.array = []

    #This is to insert a new element
    def insert(self, item):
        self.array = self.array + [item]
    #This is to remove a element
    def remove(self, item):
        for i in range(len(self.array)):
            if self.array[i] == item:
                index_to_remove = i
            
        new_array = []
        for k in range(len(self.array)):
            if k != index_to_remove:
                new_array.append(self.array[k])
                
        self.array = new_array
    #This is to remove an element at a given index
    def removeAtIndex(self, index):
        pass
    #This is to get the index of an element
    def getIndex(self, item):
        for i in range(len(self.array)):
            if self.array[i] == item:
                print(i)
    #This is to print the array contents
    def printArray(self):
        print(self.array)

test_array = Array()
test_array.insert(2)
test_array.insert(3)
test_array.insert(4)
test_array.insert(5)
test_array.insert(6)

test_array.getIndex(3)

test_array.printArray()