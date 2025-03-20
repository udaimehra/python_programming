# Python code below
# Efficient program to find all the prime numbers upto given num.
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    # Your code goes here.
    primeList = []
    x = len(primeList)
    isPrime = False
    for factor in range(2, num):
        if len(primeList) >0:
            for i in primeList:
                if factor % i != 0:
                    isPrime = True
                else:
                    isPrime = False
                    break;
            if isPrime:
                primeList.append(factor)
        else:
            primeList.append(factor)
    print(primeList)
    return primeList
    pass

num = 50
result = Answer.allPrimesUpTo(num)
