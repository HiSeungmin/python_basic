a = int(input())
arr = []

for i in range(a):
    b = list(map(int,input().split()))
    arr.append(b) 

res = []
for s in range(a):
    k = 1
    for i in range(a):
        if (s == i):
            continue
        elif arr[s][0] < arr[i][0] and arr[s][1] < arr[i][1]:
            k += 1
    print(k, end = " ")   
    #res.append(k)

#print(res)