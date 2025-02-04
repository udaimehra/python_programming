largest=None
smallest=None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    elif num == "bob":
        message = "Invalid input"
    else:
        try:
            inum = int(num)
            print(inum+1)
            if inum > largest:
                largest = inum
            if inum < smallest:
                smallest = inum
        except:
            message = "Invalid input"
print(message)
print("Maximum", largest)
print("Minimum", smallest)