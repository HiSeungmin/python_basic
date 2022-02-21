# Section05_2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :",v2)

for v3 in range(1,11):
    print("v3 is :",v3)
print()

# 1 ~ 100 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1,101)))
print('1 ~ 100 : ', sum(range(1,101,2))) #짝수만 구하기, 2씩 건너 뛰어라.

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전 -> 모두 반복 가능
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ["kim", "Park", "Cho", "Choi", "Yoo"]

for name in names:
    print("You are : ", name)

word = "dreams"

for s in word:
    print("Word : ",s)

my_info = {
    "name" : "Kim",
    "age" : 33,
    "city" : "Seoul"
}

# 기본 값 : 키
for key in my_info: 
    print("my_info : ", key)

# 키
for key in my_info.keys():
    print("my_info : ", key)

# values
for key in my_info.values():
    print("my_info : ", key)

# 키 and 값
for k,v in my_info.items():
    print("my_info : ", k, v)

# 소문자->대문자, 대문자->소문자로 바꿔서 출력해라
name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break    # 더이상 순회를 하지 않음.
    else:
        print("not found : 33!")

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
    if num == 33:
        print("found : 33!")
        break   
    else:
        print("not found : 33!")
else:
    print("Not found 33.................")


# continue

lt = ["1",2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ",type(v))


name = "Niceman"
print(list(reversed(name)))
print(tuple(reversed(name)))    