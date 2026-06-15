class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer1 = 0
        answer2 = 0
        for x in nums1:
            if x in nums2:
                answer1 += 1
        for x in nums2:
            if x in nums1:
                answer2 += 1
        return [answer1, answer2]
