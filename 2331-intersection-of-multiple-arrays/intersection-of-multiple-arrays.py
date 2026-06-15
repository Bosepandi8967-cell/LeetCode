class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        common = set(nums[0])        
        for current_list in nums[1:]:
            common = common.intersection(current_list)
        return sorted(list(common))
