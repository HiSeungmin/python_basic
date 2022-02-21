# a, b = map(int,input().split())
# a = list(map(int,input().split())) 입력받은 수를 리스트에 넣는다.
# a = int(input()) 

num = int(input())
arr = []
for k in range(10001):
    arr[k].append(0)

for i in range(num):
    b = int(input())
    arr[b] += 1

for i in range(10001):
    for j in arr[i]:
        print(i)


# a = int(input("입력>>"))
# b = []
# for i in range(a):
#     b.append(int(input()))

# b.sort()

# for i in b:
#     print(i)