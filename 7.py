n = int(input())
name_lst = []
time_lst = []
plce_lst = []
for i in range(n):
    user = list(map(str,input().split()))
    name,place,time = user[0], user[-3], user[-1]
    time_set = (int(time[0]+time[1]) * 60) + int(time[-2] + time[-1])
    name_lst.append(name)
    time_lst.append((time, time_set))
    plce_lst.append(place)
    
    
for i in range(n):
    
    for j in range(n-i-1):
        if name_lst[j] > name_lst[j+1]:
            time_lst[j], time_lst[j+1] = time_lst[j+1], time_lst[j]
            name_lst[j], name_lst[j + 1] = name_lst[j + 1], name_lst[j]
            plce_lst[j], plce_lst[j + 1] = plce_lst[j + 1], plce_lst[j]
    
            
        if name_lst[j] == name_lst[j+1]:
            if time_lst[j][1] < time_lst[j + 1][1]:
                time_lst[j], time_lst[j + 1] = time_lst[j + 1], time_lst[j]
                plce_lst[j], plce_lst[j + 1] = plce_lst[j+1], plce_lst[j ]
    
    
    
    
    
    
for i in range(n):
    print(f"{name_lst[i]} will departure for {plce_lst[i]} at {time_lst[i][0]} ")