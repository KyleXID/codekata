# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) == 0:
            nums1 = nums2
        elif len(nums2) != 0:
            nums1.extend(nums2)

        nums1.sort()

        if len(nums1) % 2 == 1:
            median = float(nums1[((len(nums1)+1)//2)-1])
        else:
            median = (nums1[len(nums1)//2-1]+nums1[len(nums1)//2])/2

        return median


class Solution:  # 다른 방법
    def findMedianSortedArrays(self, nums1, nums2):
        newNums = nums1 + nums2

        newNums.sort()

        value = len(newNums)

        if (value % 2) == 0:
            num1 = newNums[value//2 - 1]
            num2 = newNums[value//2]
            return (num1 + num2)/2
        else:
            return float(newNums[value//2])

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
