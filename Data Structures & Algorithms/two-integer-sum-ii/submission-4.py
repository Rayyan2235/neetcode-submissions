'''
Pattern: Most efficient is 2 pointers
Key Words: "1 Indexed" index starts from 1 rather than usual where it starts from 0
    "non-decreasing" means ascending, allows duplicates.

LOGIC: 
    Since the list is in ascending order, if numebrs[l] +numebrs[r] is greater than target
    then numbers[r] must be the issue as its too large therefore must decrease r and vice versa


    Iterate over numbers
    since in ascending order so add the 2 pointers, 
    if result greater than target
    move r -=1, vice versa
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:



        mp = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in mp:  # Check if key exists
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
            
        


'''
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    count = defaultdict(int) # The number: index + 1
    for i in range(len(numbers)):
        mp = target - numbers[i]
        if count[mp]:
            return [count[mp], i + 1]
        count[numbers[i]] = i + 1 #Since we are storing as 1 indexed     

'''
           

    






        