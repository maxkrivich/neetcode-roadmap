class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_inx = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums_inx and i != nums_inx[dif]:
                return [i, nums_inx[dif]]
        return [-1, -1]
"""
nums = [2,7,11,15], target = 9
nums_ids = {2:0, 7:1, 11: 2, 15: 3}
diffs = [7, 2, 2, 6]
"""
