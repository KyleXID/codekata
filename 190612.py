# 190612codekata https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    result = [i, j]
                    return result


"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# https://leetcode.com/problems/add-two-numbers/solution/
# 2. Add Two Numbers


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    str_l1, str_l2 = '', ''
    while l1:
        str_l1 += str(l1.val)
        l1 = l1.next
    while l2:
        str_l2 += str(l2.val)
        l2 = l2.next
    int_l1 = int(str_l1[::-1])
    int_l2 = int(str_l2[::-1])
    return list(map(int, str(int_l1 + int_l2)[::-1]))


"""
You are given two non-empty linked lists
representing two non-negative integers.
The digits are stored in reverse order and
each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
