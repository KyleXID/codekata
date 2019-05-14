# Day20.Week5(day2) Selection Sort(선택정렬) 정렬되지 않은 데이터 중 가장 작은 데이터를 선택해서 맨 앞에서부터 순서대로 정렬해 나가는 함수입니다.

def selectionSort(nums):
  for i in range(len(nums)):
    min_idx = i
    for j in range(i+1, len(nums)):
      if nums[min_idx] > nums[j]:
          min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]

  return nums


# 다른 방법

def selectionSort(nums):

  for i in range(0, len(nums)-1):

    minnum = min(nums[i:])
    nums.remove(minnum)
    nums.insert(i, minnum)
  
  return nums

print(selectionSort([7,5,4,2,10,11,1]))
