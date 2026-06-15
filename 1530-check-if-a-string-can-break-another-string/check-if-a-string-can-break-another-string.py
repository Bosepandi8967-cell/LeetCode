class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        
        s1_breaks = True
        s2_breaks = True
        for i in range(len(s1)):
            if s1_sorted[i] < s2_sorted[i]:
                s1_breaks = False
            if s2_sorted[i] < s1_sorted[i]:
                s2_breaks = False
                
        return s1_breaks or s2_breaks

