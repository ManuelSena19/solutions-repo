class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        sum_freq = {0: 1}
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]
            sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
            
        return count
        