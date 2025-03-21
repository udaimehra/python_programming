# Python code below
# This program is to find out the square of a number by using only the 
# triangle function given below.

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    numSquare = (triangle(num)+triangle(num))-num
    print(numSquare)
    return numSquare
    pass

#Answer.square(5)
answer = square(5)
print(answer)
