class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        count_dict = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in count_dict:
                count_dict[num] = i
        
        return [count_dict[num] for num in nums]