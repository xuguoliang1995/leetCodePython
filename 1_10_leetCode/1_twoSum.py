# /usr/bin/env python3
# encoding: utf-8

"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:
    @classmethod
    def twoSum(self, nums, target):
        '''
        :param nums:
        :param target:
        :return: List(int)
        time: O(n)
        space: O(n)
        '''
        dic = {}
        for index, value in enumerate(nums):
            n = target - value
            if n in dic:
                return [index, dic[n]]
            dic[value] = index
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    nums = Solution.twoSum(nums, target)
    print(nums)
