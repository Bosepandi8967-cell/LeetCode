class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        total_len = len(merged)
        if total_len % 2 == 1:
            return float(merged[total_len // 2])
        else:
            mid1 = merged[(total_len // 2) - 1]
            mid2 = merged[total_len // 2]
            return (mid1 + mid2) / 2.0
