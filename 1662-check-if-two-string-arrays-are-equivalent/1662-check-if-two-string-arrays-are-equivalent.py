class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        string1 = ''
        string2 = ''

        for word in word1:
            string1 += word

        for word in word2:
            string2 += word

        if string1 == string2:
            return True
        else:
            return False
        