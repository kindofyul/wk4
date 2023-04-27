n, x = map(int,input().split())
num = list(map(int, input().split()))

i = 0
for i in range (0, n):
    if x < num[i]:
        print(num[i], end = " ")