# Day11.week3(day1) 두개의 복소수를 string형의 input으로 받아, 두 수를 곱해서 반환하는 함수입니다. 반환하는 값도 string형이여야합니다.

def complexNumberMultiply(a, b):
  plus = a.index("+")
  plus2 = b.index("+")
  
  num1 = int(a[:plus])
  num2 = int(a[(plus+1):(len(a)-1)])
  num3 = int(b[:plus2])
  num4 = int(b[(plus2+1):(len(b)-1)])
  
  com1 = str((num1 * num3) - (num2 * num4))
  com2 = str((num2 * num3) + (num1 * num4))
  
  result = com1 + "+" + com2 + "i"
  
  return result
  
print(complexNumberMultiply("1+1i","1+1i"))

# 짧은 버전
#def complexNumberMultiply2(a, b):
#  """
#  :type a: str
#  :type b: str
#  :rtype: str
#  """
#  a1, a2 = map(int, a[:-1].split('+'))
#  b1, b2 = map(int, b[:-1].split('+'))
#  return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)

# 다른 버전
#def complexNumberMultiply(a, b):
#  """
#  :type a: str
#  :type b: str
#  :rtype: str
#  """
#
#  firstArr = a[:-1].split('+')
#  a1 = int(firstArr[0])
#  a2 = int(firstArr[1])
#
#  secondArr = b[:-1].split('+')
#  b1 = int(secondArr[0])
#  b2 = int(secondArr[1])
#
#  return f'{a1 * b1 - a2 * b2}+{a1 * b2 + a2 * b1}i'
