class Solution(object):
    def productExceptSelf(self, nums):
        answer = [0] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer