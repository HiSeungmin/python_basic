# Section04_4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서X, 중복X(Key는 안되고 값은 중복가능), 수정X, 삭제O 

# Key, Value (Json) -> MongoDB
# 선언
a = {'name' : 'Kim', 'phone' : '010-0000-0000', 'birth' : 980201}
b = {0 : 'Hello Python', 1 : 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'])
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

# keys, values, items(key와 values의 한 쌍)
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))
print()

print(list(a.items()))
print(1 in b)
print('name' in a)
print('name2' not in a)
print()

# 집합(sets) (순서X, 중복X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c) # 중복하지 않고 출력됨.

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2)) # 합집합

print(s1 - s2) # 차집합
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
# s3.add(7) 이미 있어서 값에 영향을 주지 않음.

print(s3)

s3.remove(15)
print(s3)

print(type(s3))