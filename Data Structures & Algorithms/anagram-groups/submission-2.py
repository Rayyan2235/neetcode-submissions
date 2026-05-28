class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Key value = sorted  letters : all the words w the anagram
        """
        res = defaultdict(list)
        for i in strs:
            a = ''.join(sorted(i))
            res[a].append(i)
        return list(res.values())
