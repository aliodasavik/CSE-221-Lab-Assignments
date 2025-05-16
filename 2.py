user = int(input())
for i in range(user):
    n = list(map(str,input().split()))
    if n[2] == "+":
    
        print(int(n[1]) + int(n[3]) )
    elif n[2] == "-":
    
        print(int(n[1]) - int(n[3]) )
    elif n[2] == "*":
    
        print(int(n[1]) * int(n[3]))
    
    else:
        print(int(n[1]) / int(n[3]))