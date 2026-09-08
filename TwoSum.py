target = 9

def findTwoSum(nums):
    hashmap = {}
    
    for index, number in enumerate(nums):
        if (target - number) in hashmap:
            print([hashmap[target - number], index])
        hashmap.update({number : index})
    return

listofNums = [2,7,11,15]
findTwoSum(listofNums)
