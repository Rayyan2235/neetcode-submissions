class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        need = len(t_count)   # unique chars we must satisfy
        have = 0              # unique chars we've currently satisfied

        window = {}           # char counts in current window
        result = ""
        result_len = float("inf")
        l = 0

        for r in range(len(s)):
            # 1. add character to window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # 2. check if this char just became fully satisfied
            if c in t_count and window[c] == t_count[c]:
                have += 1

            # 3. while window is valid, try shrinking from left
            while have == need:
                # update result if this window is smaller
                if (r - l + 1) < result_len:
                    result_len = r - l + 1
                    result = s[l:r+1]

                # shrink from left
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        return result