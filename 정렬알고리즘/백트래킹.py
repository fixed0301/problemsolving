h, m = map(int, input().split())
time = int(input())

m += time

h += m//60
m = m % 60

if h > 24:
    h -= 1
if h == 24:
    h =0
print(h, m)