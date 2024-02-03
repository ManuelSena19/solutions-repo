class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter = ''
        s_counter = {}
        t_counter = {}

        for char in s:
            s_counter[char] = s_counter.get(char, 0) + 1

        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        for char, count in t_counter.items():
            if char not in s_counter or count != s_counter[char]:
                letter = char
                break
        
        return letter
        