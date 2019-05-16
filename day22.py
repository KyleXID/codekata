# Day22.Week5(day4) 재귀(Recursion) 함수 실행 내부에서 자가함수를 다시 호출하여 str의 형태를 거꾸로 배치한 값을 반환하는 값입니다.

def reverseString(str):
  if len(str) == 0:
    return ''
  else:
    str = list(str)
    a = str.pop()
    str = ''.join(str)
    return a+reverseString(str)

#다른 방법

def reverseString(str):
  if len(str) == 0:
    return str
  else:
    return reverseString(str[1:]) + str[0]
