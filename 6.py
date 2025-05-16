user = int(input())
id = list(map(int,input().split()))
num = list(map(int,input().split()))
sorted_id = []
sorted_marks = []
count = 0
for i in range(user):
    max = i
    min_id = -9999
    for j in range(i + 1, user):
        if num[j] > num[max]:
            max = j
        if num[max] == num[j] and id[j] < id[max]:
            max = j
    
    if i != max:
        num[i], num[max] = num[max], num[i]
        id[i], id[max] = id[max], id[i]
        count += 1
    
print(f"Minimum swaps: {count}")
    
for i in range(user):
    print(f"ID: {id[i]} Mark: {num[i]}")