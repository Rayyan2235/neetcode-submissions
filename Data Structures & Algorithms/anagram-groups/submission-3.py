class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Create a dict where values is a list
        for s in strs:
            count = [0] * 26 # 26 letters
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # count array is the key and the string appended is the value
        return list(res.values())


        