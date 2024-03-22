class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        p_freq = {}
        s_freq = {}

        for char in p:
            if char in p_freq:
                p_freq[char] += 1
            else:
                p_freq[char] = 1

        start = 0
        count = 0

        for end in range(len(s)):
            if s[end] in s_freq:
                s_freq[s[end]] += 1
            else:
                s_freq[s[end]] = 1

            if s[end] in p_freq and s_freq[s[end]] <= p_freq[s[end]]:
                count += 1

            if end - start + 1 > len(p):
                if s[start] in s_freq:
                    s_freq[s[start]] -= 1
                    if s_freq[s[start]] < p_freq.get(s[start], 0):
                        count -= 1
                start += 1

            if count == len(p):
                result.append(start)

        return result