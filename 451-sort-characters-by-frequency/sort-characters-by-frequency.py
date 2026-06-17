from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        ordered_pairs = counts.most_common()
        result = ""
        for char, count in ordered_pairs:
            result += char * count         
        return result
        