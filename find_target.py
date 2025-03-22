# This program is to find the target of sum of two numbers in 
# the list and output the number positions in a list.
class Solution(object):
    def __init__(self, name):
        self.name = name

    def twoSum(self, nums, target):
        rList = []
        found = False
        listEnd = len(nums)
        message = "None found for the given target"
        for i in range(listEnd-1):
            for n in range(i+1,listEnd):
                if nums[i] + nums[n] == target:
                    found = True
                    break;
            if found == True:
                break;
        if found == True:
            rList.append(i)
            rList.append(n)
            return rList
        else:
            return message

if __name__ == "__main__":
    function_name = "finder"
    n = [1,1,1,1,1,1,1,1,3,3]
    t = 6
    ts = Solution(function_name)
    result = ts.twoSum(n, t)
    print("The result is", result)
                
        
