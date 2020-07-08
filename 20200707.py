"""
괄호가 n쌍인 괄호의 모든 조합을 생성하여 리스트로 리턴하는 함수를 작성하라.

ex)
n = 3
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        s = [("(", 1, 0)]

        while s:
            x, l, r = s.pop()

            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)

            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))

        return res
