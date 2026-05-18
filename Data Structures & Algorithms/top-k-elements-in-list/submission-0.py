class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        arr = []
        for num, cnt in m.items():
            arr.append([cnt, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res