class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
Core Intuition:

You’re maintaining a moving window of characters that have no duplicates.

Expand the window by adding characters to the right.

If a duplicate appears, shrink the window from the left until it’s valid again.

Keep track of the maximum window length seen so far.


        '''
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res
        '''
Key Takeaways:

Use Sliding Window whenever you need the longest/shortest substring/subarray that satisfies a condition.

while loop removes old characters until the window becomes valid again.

Skill learned: Efficient window adjustment and condition maintenance.

Common trap: Returning early when a duplicate is found (must continue scanning).
        '''
            
        