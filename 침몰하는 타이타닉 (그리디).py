# 침몰하는 타이타닉 (그리디)

import sys
from collections import deque
# 데크를 쓰는이유? 리스트를 만들어서 앞의 요소를 pop해주면 뒤 인덱스 요소들이 하나씩 앞으로 당겨오는 비효율적인 구조가 된다.
# 이를 막기 위해 각 포인터만 변경해주는 데크를 사용한다.

# sys.stdin = open("in1.txt", "r")

N, M = map(int, input().split())
wt_list = list(map(int, input().split()))
wt_list.sort()
wt_list = deque(wt_list)
cnt = 0

while wt_list:
    if len(wt_list) == 1:
        cnt += 1
        break

    if wt_list[0] + wt_list[-1] > M:
        wt_list.pop()
        cnt += 1
    else:
        wt_list.popleft()
        wt_list.pop()
        cnt += 1



# for i in wt_list:
#     if (boat_wt + i) < M:
#         boat_wt += i
#     else:
#         boat_wt = 0
#         cnt += 1

print(cnt)



"""
유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고
있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있
으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는
프로그램을 작성하세요.

▣ 입력설명
첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.

▣ 출력설명
첫째 줄에 구명보트의 최소 개수를 출력합니다.

▣ 입력예제 1
5 140
90 50 70 100 60

▣ 출력예제 1
3
"""