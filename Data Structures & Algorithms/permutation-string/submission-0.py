class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Permutation - order doesnt matter

        so if we store s1 in a dictionary with its freq
        get the length of it, therefore the window will be the size of s1

        '''
        count = {}
        for i in s1:
            count[i] = 1 + count.get(i , 0)

        need = len(count)
        for i in range(len(s2)):
            count2, curr = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                # used  count.get(s2[j], 0) to check if the item is in the first dict (s1)
                if count.get(s2[j], 0) < count2.get(s2[j]):
                    break
                if count.get(s2[j], 0) == count2.get(s2[j]):
                    curr += 1
                if curr == need:
                    return True
        return False


        