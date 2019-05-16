# Day21.Week5(day3) 버블정렬(Bubble Sort) 인접한 데이터를 교환해서 정렬하는 알고리즘입니다.

def bubbleSort(arr):
  for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
      else:
        i +=1

  return arr

# 비슷하지만, 다른 방법
def bubbleSort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]
