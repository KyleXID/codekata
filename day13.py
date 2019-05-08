# Day13.Week3(day3) 양수로 이루어진 m x n 그리드를 인자로 받습니다. 상단 왼쪽에서 시작하여 하단 오른쪽까지 가는 길의 요소를 다 더했을 때 가장 작은 합을 찾아 반환하는 함수입니다.

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(1, n):
        grid[0][i] += grid[0][i-1]

    for i in range(1, m):
        grid[i][0] += grid[i-1][0]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]
