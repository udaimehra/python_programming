# Example of extending the class list. The use of list 
# variable in class definition indicates that we are 
# extending a list with few more methods.

class UniqueList(list):
           
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'

    def append(self, item):
        if item in self:
            return
        super().append(item)  

mylist = UniqueList()
mylist.append(1)
mylist.append(1)
mylist.append(2)
print(mylist.someProperty)
print(mylist)
