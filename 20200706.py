"""
2n의 길이로 이루어진 nums 리스트가 주어진다. 이 리스트를 다음과같이 return 하는 함수를 작성하라.
[x1,x2,...,xn,y1,y2,...,yn]
[x1,y1,x2,y2,...,xn,yn]
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a1 = nums[:n]
        a2 = nums[n:]

        new_array = []

        for i in range(0, n):
            new_array.append(a1[i])
            new_array.append(a2[i])

        return new_array


class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res
