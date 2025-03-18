# List comprehension example
myList = list(range(100))
FilteredList = [item for item in myList if item % 10 == 0]
print(FilteredList)
newString = 'My name is Udai Singh Mehra. I live in New Delhi.'
newList = newString.replace('.', '').lower().split(' ')
print(type(newList))
list3 = []
[list3.append(item) for item in newList if len(item) <=3]
for item in newList:
    if len(item) <=3:
        print(item)
print(list3)
