class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(curr_sum, curr_sum + num)
            max_sum = max(curr_sum, max_sum)

        return max_sum