class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        target_indices = []
        
        for i, num in enumerate(sorted_nums):
            if num == target:
                target_indices.append(i)
        
        return target_indices

        