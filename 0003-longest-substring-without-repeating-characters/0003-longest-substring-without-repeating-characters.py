class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        index = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in index and index[s[end]] >= start:
                start = index[s[end]] + 1
            index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length