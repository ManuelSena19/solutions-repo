class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_len = float('inf')
        arr_sum = 0
        left = 0

        for right in range(n):
            arr_sum += nums[right]
            
            while arr_sum >= target:
                min_len = min(min_len, right - left + 1)
                arr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0