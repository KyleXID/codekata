# Day24.Week6(day3) 2019 카카오 신입 공채 1차 코딩 테스트 2번

def solution(N, stages):
  newstages = []
  dic = {}
  count = 0

  for i in range(1,N+1):
    newstages.append(i)

  for stage in newstages:
    count = 0

    for i in range(len(stages)):
      if stage <= stages[i]:
        count += 1

    failuser = stages.count(stage)

    if count == 0:
      dic[stage] = 0
    else:
      dic[stage] = failuser/count
    print(failuser,"/",count)

  print(dic)
  result = sorted(dic, key=lambda k : dic[k], reverse=True)

  return result

print(solution(5, [2,1,2,6,2,4,3,3]))

  #실패율 : 도달했으나 클리어하지못한 유저수 / 스테이지 도달한 플레이어 유저수
