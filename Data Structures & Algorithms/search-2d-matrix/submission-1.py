class Solution:
    def binary_search(self, l: int, r: int, matrix: List[List[int]], target: int) -> int:
        flat = [num for row in matrix for num in row]
        if l > r:
            return False
        m = l + (r - l) // 2
        if flat[m] == target:
            return True
        if flat[m] < target:
            return self.binary_search(m + 1, r, matrix, target)
        return self.binary_search(l, m - 1, matrix, target)
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [num for row in matrix for num in row]
        return self.binary_search(0, len(flat) - 1, matrix, target)