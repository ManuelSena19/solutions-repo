class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        prefix = strs[0]

        for char in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(char) and prefix[i] == char[i]:
                i += 1
            prefix = prefix[:i]
            if not prefix:
                return ''

        return prefix
        