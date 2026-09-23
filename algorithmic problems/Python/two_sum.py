class Solution(object):
    def twoSum(self, nums, target):
        visited = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [visited[diff], index]
            visited[num] = index

        return []