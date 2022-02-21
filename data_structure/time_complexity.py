# 1 ~ n의 합을 구하는 알고리즘 / 시간 복잡도 : O(n)
def sum_all(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total

print(sum_all(10))

# 1 ~ n의 합을 구하는 알고리즘2 => n*(n+1)/2 / 시간 복잡도 : O(1)
def sum_all2(n):
    return int(n*(n+1)/2)

print(sum_all2(10))