# Python code below

def encodeString(stringVal):
    # Your code goes here.
    #print(len(stringVal))
    prevChar = None
    charCount = 0
    newList = []
    i = 0
    for char in stringVal:
        if char != prevChar:
            #print(f'New character is {char} and value is {charCount}')
            newList.append(char)
            prevCharCount = charCount
            charCount = 1
            prevChar = char
        else:
            charCount = charCount + 1
        #print(f'Continued character is {char} and its count is {charCount}')
    #print(f'Unique list is {newList}')
    fullList = list(stringVal)
    #print(f'Original list is {fullList}')

    uc = len(newList)-1
    oc = len(fullList)-1
    i = 0
    j = 0
    myset = []
    #print(uc, oc)
    while i <= uc:
        count = 0
        while j <= oc:
            if newList[i] == fullList[j]:
                count = count + 1
                #print(f'{newList[i]} and {fullList[j]} are matching and count is {count}')
                j = j + 1           
            else:
                #print(f'final count of {newList[i]} is {count}')
                myset.append((newList[i], count))
                count = 0
                #print('count reset to 0')
                break;
        if i == uc:       
            #print(f'final count of {newList[i]} is {count}')
            myset.append((newList[i], count))
        i = i + 1
    print(myset)
    return myset
    pass

    
def decodeString(encodedList):
    # Your code goes here.
    mystring = ''
    for i in encodedList:
        #print(i[0], i[1])
        mystring = mystring + i[0]*i[1]
    print(mystring)
    return mystring
    pass


# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
art = 'AAAAABBBBAAACCDDDD'
encoded = Answer.encodeString(art)
decoded = Answer.decodeString(encoded)

