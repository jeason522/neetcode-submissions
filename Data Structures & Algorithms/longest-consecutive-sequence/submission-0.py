class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cnt = 1
        max_cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                max_cnt = max(cnt, max_cnt)
                cnt = 1
        return max(cnt, max_cnt)