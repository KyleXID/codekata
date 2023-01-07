import sys
import heapq # 최솟값부터 풀어야하는 특성때문에 힙을 써준다.


N, M= map(int, sys.stdin.readline().rstrip().split())

# 각 번호(노드)에 대한 진입차수 초기화
in_degree = [0] * (N + 1)
# 번호에 우선 풀어야할 번호의 정보를 담는 연결리스트 (간선 정보)
graph = [[] for _ in range(N +1)]

# 진입차수와 간선 정보를 입력한다
for _ in range(M):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    graph[first].append(second)
    # 간선정보를 입력하면서 진입차수를 추가해준다.
    in_degree[second] += 1

q = []

def sort_test_list():
    result = []

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            # 문제에 먼저 풀어야 할 문제가 없는 경우 큐에 넣어준다.
            heapq.heappush(q, i)

    while q:
        # 적은 수부터 먼저 풀어야하기 때문에 최소값을 뽑아준다.
        now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            # 큐에서 뽑아낸 문제와 연결된 문제의 간선을 -1 해준다.
            in_degree[i] -= 1

            # 문제에 먼저 풀어야 할 문제가 없는 경우 큐에 넣어준다.
            if in_degree[i] == 0:
                heapq.heappush(q, i)

    new_test_list = [str(test_number) for test_number in result]
    
    return ' '.join(new_test_list)

print(sort_test_list())