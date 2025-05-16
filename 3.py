N,k = map(int,input().split())
j = N -1
lst = list(map(int,input().split()))
for i in range(N//2):
    lst[i], lst[j] = lst[j], lst[i]
    j -= 1
i = N - k
while i < N:
    print(lst[i], end= " ")
    i += 1