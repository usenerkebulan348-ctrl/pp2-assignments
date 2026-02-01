a, b, c = map(int, input().split())
n = list(map(int, input().split()))


n[b-1:c] = reversed(n[b-1:c])

print(*n)
