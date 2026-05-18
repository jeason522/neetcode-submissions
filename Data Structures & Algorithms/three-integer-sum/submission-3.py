class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -nums[i] - nums[j]
                if target in seen:
                    tmp = [nums[i], target, nums[j]]
                    res.add(tuple(tmp))
                seen.add(nums[j])
        return [list(i) for i in res]