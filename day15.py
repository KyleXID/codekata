# Day15.Week4(day1) 양수 N을 이진법으로 바꿨을 때, 연속으로 이어지는 0 중에서 가장 큰 값을 반환하는 함수입니다.

def solution(N):
  binaryNumber = format(N, 'b')
  maximum = 0
  binaryNumberList = binaryNumber.strip('0').split('1')

  for x in binaryNumberList:
    if not x:
      continue
    if len(x) > maximum:
      maximum = len(x)

  return maximum

print(solution(3243))
