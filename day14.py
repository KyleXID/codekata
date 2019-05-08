# Day14.Week3(day4) 주어진 숫자 배열에서, 0을 배열의 마지막으로 이동시키는 함수입니다. 원래 있던 숫자의 순서는 변하지 않아야 합니다.

def moveZeroes(nums):
  number = 0

  while number <= nums.count(0):
    number += 1
    nums.remove(0)
    nums.insert(len(nums), 0)
  return nums


# 다른 방법

def moveZeroes(nums):
  last0 = 0

  for i in range(0, len(nums)):
    if nums[i] != 0:
      nums[i], nums[last0] = nums[last0], nums[i]
      last0 += 1

  return nums
