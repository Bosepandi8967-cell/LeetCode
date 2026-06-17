class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for current in intervals:
            last_end = merged[-1][1]
            if current[0] <= last_end:
                merged[-1][1] = max(last_end, current[1])
            else:
                merged.append(current)
        return merged
