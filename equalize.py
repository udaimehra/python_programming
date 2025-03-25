''' You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.
'''

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        response = None
        countList = {}
        uniqLetters = []
        uniqLetterCount = []
        wrdList = list(word.lower())
        uniqLetterSet = set(wrdList)
        uniqLetterList = list(uniqLetterSet)
        #print("Unique Letter List is ", uniqLetterList, len(uniqLetterList))

        # Create the dictionary for each letter count
        for i in wrdList:
            countList[i] = wrdList.count(i)
        #print("Dictionary of words and counts is created", countList)

        # Create a list of counts for each letter
        for keys in countList:
            uniqLetterCount.append(countList[keys])
            uniqLetterCount.sort()
        uniqCounts = len(uniqLetterCount)
        #print("Unique Letter Count list is", len(uniqLetterCount), uniqLetterCount)

        uniqCountSet = set(uniqLetterCount)
        #print("Set of Unique Counts of each letter is set ", uniqCountSet)
        #print("Count of Unique Letters is ", uniqCounts)

##########################
        #Logic starts here
##########################
        if len(uniqCountSet) > 2 :
            print("Total unique letters is more than 2 and their count is also different", uniqCountSet)
            response = False
        elif len(uniqCountSet) == 1:
            print(uniqLetterCount[0], len(uniqCountSet))
            if uniqLetterCount[0] > 1 and len(uniqCountSet) == 1 and len(uniqLetterList) > 1:
                print("List has equal count and has multiple letters", len(uniqCountSet), uniqLetterCount[0])
                response = False
            elif uniqLetterCount[0] == 1 and len(uniqCountSet) == 1 and len(uniqLetterList) > 1:
                print("List has only multiple unique letters with one count only")
                response = True
            elif len(uniqLetterList) == 1:
                print("It has only one letter in the whole string with one more count")
                response = True
            else:
                response = False
## Focus on this area only - Start
        elif len(uniqCountSet) == 2 and uniqCounts == 2:
            uniqCountList = list(uniqCountSet)
            print(uniqCountList[0], uniqCountList[1])
            lastLetterCount = wrdList.count(uniqLetterList[1])
            firstLetterCount = wrdList.count(uniqLetterList[0])
            #print("List has only two unique counts", firstLetterCount, lastLetterCount)
            if uniqCountList[1]-uniqCountList[0] == 1 or (lastLetterCount == 1 or firstLetterCount == 1) :
                print("List has only two unique counts", firstLetterCount, lastLetterCount)
                response = True
            elif uniqCountList[1]-uniqCountList[0] > 2:
                response = False 
        elif uniqCounts > 2:
            uniqCountList = list(uniqCountSet)
            print(uniqCountList[0], uniqCountList[1])
            lastLetterCount = wrdList.count(uniqLetterList[1])
            firstLetterCount = wrdList.count(uniqLetterList[0])
            print("11List has only two unique counts", firstLetterCount, lastLetterCount)
            if uniqCountList[1] - uniqCountList[0] > 1:
                print("Hello")
                response = False 
            else:
                response = True 
        else:
            print("None Found")
            response = False
## Focus on this area only - End
        return response

mywrd = Solution()
testcases = ["abccdeff", "aazzdd", "aaccc", "aaabbc", "abcd", "abbbcccd", "aabbccc", "abbcc", "cbccca", "zz", "cccd"]
#testcases = ["abccdeff", "abbbcccd", "cbccca"]
for i in testcases:
    inp = i
    print(inp, "-----------")
   
    result = mywrd.equalFrequency(inp)
    print(result)
