"""
input 리스트를 k만큼 오른쪽으로 이동시켜서 반환하라, k는 양수이다.
ex)
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) <= 1:
            return nums

        target = nums

        for i in range(0, k):
            rt_target = target.pop()
            target.insert(0, rt_target)
        return target


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
