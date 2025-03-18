# List comprehension example
myList = list(range(100))
FilteredList = [item for item in myList if item % 10 == 0]
print(FilteredList)

newString = 'My name is Udai Singh Mehra. I live in New Delhi'
newList = newString.replace('.', '').lower().split()

list3 = []
[list3.append(item) for item in newList if len(item) <=3]
print(list3)

myList1 = []
sent = []
myList1 = [[sent] for sent in newString.split('.')] 
print(type(myList1))
print(myList1)

myList = []
myList = [[word for word in sentence.split()] for sentence in newString.split('.')] 
print(type(myList))
print(myList)
