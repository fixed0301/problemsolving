#백트래킹은 dfs이다!
import sys
input = sys.stdin.readline
N = int(input())
s = []
for x in range(N):
    s.append(list(map(int, input().split())))

def nung(x, y):
    return s[x-1][y-1]

#두 팀 능력치의 차이가 최소가 되려면 어케할까
'''
1. 사람 골라넣는데 visited 리스트에서 방문처리하며 재귀함수 형태
2. n//2 명 다 채워지면 그때 총합 구하기
3. 방문처리되면 스타트, 안되면 링크로 능력치 계산
4. 능력치 차이의 절댓값 비교해가며 갱신
'''
def dfs(depth, idx):
    if depth == N//2:


    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs()

