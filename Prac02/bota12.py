a=int(input())
n = list(map(int, input().split()))

for i in range(a):
    n[i]=n[i]*n[i]
print(*n)