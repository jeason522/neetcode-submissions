class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            window = right - left + 1
            max_cnt = max(count.values())
            while window - max_cnt > k:
                count[s[left]] -= 1
                left += 1
                window = right - left + 1
            res = max(res, right - left + 1)
        return res