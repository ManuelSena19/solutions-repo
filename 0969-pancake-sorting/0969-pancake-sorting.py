class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result, n = [], len(arr)
        for x in range(n, 0, -1):
            i = arr.index(x)
            result.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return result