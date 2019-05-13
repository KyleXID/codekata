# Day18.Week4(day4) 숫자로 이루어진 리스트를 인자로 받아 그 안에서 연속적 요소를 더했을 때 가장 큰값을 찾아 반환하는 함수입니다.

def maxSubArray(nums):
  maxnum = 0
  dic = {}
  
  for i in range(0,len(nums)):
    accum = nums[i]
    dic[i] = [accum]
    
    for j in range(i+1, len(nums)):
      if i == len(nums):
        dic[i] = nums[i]
      else:
        accum += nums[j]
        dic[i].append(accum)
      print(dic)
    
    dic[i] = max(dic[i])
    
  maxnum = max(dic.values())
    
  return maxnum
  
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# 다른 방법
def maxSubArray(nums):
  for i in range(1, len(nums)):
    if nums[i-1] > 0:
      nums[i] += nums[i-1]

  print(nums)
  return max(nums)

maxSubArray([-2,1, 3, 4, -3, 3])
