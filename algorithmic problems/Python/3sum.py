class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left, right = 0, len(nums) - 1

            while left < right:
                three_sum = value + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result 