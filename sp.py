n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort(key=lambda a: a[0])
time.sort(key=lambda a: a[1])
#이렇게 정렬하는 이유가 가장 짧은 회의 순으로 정렬한거네!!!!
#시작점이 작은 순으로, 끝점도 가장 작은 순으로 정렬되네

end = 0
cnt = 0
for i, j in time:
    if i >= end: #만약 다른 회의의 시작이 end보다 크다(회의가 겹치지 않음)
        end = j #end를 현재까지 회의중 제일 늦은걸로 잡고(그다음 위로)
        cnt += 1


print(time)