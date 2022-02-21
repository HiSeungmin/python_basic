# Section04_3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서O, 중복O, 수정O, 삭제O)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])
print()

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제 
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print("-------------------------------")
print(c)
del c[-1]
print(c)
print()
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 추가
print(y)
y.sort() # 정렬
print(y)
y.reverse() # 거꾸로
print(y)
y.insert(2,7) # 2번 인덱스에 7 추가
print(y)
y.remove(2) #숫자 2를 삭제
print(y)

print()

y.pop() # 마지막꺼 꺼냄 LIFO, pop()을 계속 사용하면 에러가 남.
print(y)

ex = [88, 77]
y.append(ex) # 리스트 자체를 삽입
#y.extend(ex) # y에 연장
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서O, 중복O, 수정X, 삭제X)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2]) # 인덱싱 가능

print(d[2:]) # 슬래싱도 가능
print(d[2][0:2])

print(c+d)
print(c*3)
print()

# 튜플 함수

z = (5, 2, 1, 3, 1)

print(z)
print(3 in z)
print(z.index(3)) # 3이 있는 인덱스 번호를 반환
print(z.index(5))
print(z.count(1)) # 1이 몇 개 있는지
