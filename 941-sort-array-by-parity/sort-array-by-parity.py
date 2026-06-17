class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        return evens + odds
