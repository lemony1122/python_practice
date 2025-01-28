N = int(input())
M = [int(input()) for _ in range(N)]

for i in range(N):
    print("Case #%d: %d" % (i + 1, M[i]))
