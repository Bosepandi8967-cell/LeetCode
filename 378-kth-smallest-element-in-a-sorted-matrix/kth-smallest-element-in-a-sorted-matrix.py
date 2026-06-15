class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        def count_less_equal(target):
            count = 0
            row = n - 1 
            col = 0     
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += (row + 1)
                    col += 1 
                else:
                    row -= 1 
            return count
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) >= k:
                high = mid   
            else:
                low = mid + 1
                
        return low
