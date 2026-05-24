class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums) - k + 1
        for i in range(n):
            window = nums[i:i + k]
            res.append(max(window))
        return res