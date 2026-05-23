class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        c1 = {}
        for c in t:
            c1[c] = c1.get(c, 0) + 1
        
        window = {}
        required = len(c1)
        have = 0
        left = 0
        best_len = float('inf')
        best_left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in c1 and c1[c] == window[c]:
                have += 1
            while have == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_left = left
                left_c = s[left]
                window[left_c] -= 1
                if left_c in c1 and window[left_c] < c1[left_c]:
                    have -= 1
                left += 1
            
        if best_len == float('inf'):
            return ""
        return s[best_left:best_left + best_len]