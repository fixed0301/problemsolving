# 입력값 받기
m, n, x, y = map(int, input().split())

# 땅의 비옥도 정보 입력받기
land = []
for _ in range(m):
    row = list(map(int, input().split()))
    land.append(row)

# 최대 비옥도 초기화
max_fertility = 0

# 구역 비옥도 계산
for i in range(m - x + 1):
    for j in range(n - y + 1):
        fertility = 0
        # 선택한 구역의 비옥도 합 구하기
        for k in range(i, i + x):
            for l in range(j, j + y):
                fertility += land[k][l]
        # 최대 비옥도 업데이트
        if fertility > max_fertility:
            max_fertility = fertility

# 결과 출력
print(max_fertility)
