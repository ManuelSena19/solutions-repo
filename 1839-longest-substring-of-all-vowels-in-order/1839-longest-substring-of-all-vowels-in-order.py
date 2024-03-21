class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        seen = set()
        start, max_length = -1, 0
        for end, c in enumerate(word):
            if end > 0 and c < word[end - 1]:
                seen = set()
                start = end - 1    
            seen.add(c)    
            if len(seen) == 5:
                max_length = max(max_length, end - start)
        return max_length
        