# Day19.Week5(day1) 이진 탐색(binary search) 순서대로 찾아나서는 방법이 아닌 중간부터 찾아나서는 탐색법입니다. 중간지점의 값과 타겟의 크기를 비교하여 어디로 갈지 결정하여 이동하고 다시 찾아나서는 탐색법입니다.

 def search(nums, target):
  l, r = 0, len(nums) - 1
  while l <= r:
    mid = (l + r) // 2
    if nums[mid] < target:
      l = mid + 1
    elif nums[mid] > target:
      r = mid - 1
    else:
      return mid
  return -1
