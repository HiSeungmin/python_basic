# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k in q1.keys():
    if k == "가을":
        print(q1[k])

for k, v in q1.items():
    if k == "가을":
        print(v)
    
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q2.items():
    if v =="사과":
        print(k, v, ">> 사과 있음!")
        break
    else:
        print("사과가 없습니다.")


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 99

if score >=81:
    print("A학점")
elif score >= 60:
    print("B학점")
elif score >= 41:
    print("C학점")
elif score >= 21:
    print("D학점")
else:
    print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a, b, c = 12, 6, 18
best = a
if b > a:
    best = b
if c > b:
    best = c
print('best : ',best)


num1 = 12
num2 = 6
num3 = 18
if num1>num2:
    max = num1
else:
    max = num2
if max>num3:
    print(max)
else:
    print(num3)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'
if int(s[7]) % 2 == 0:
    print("여자")
else:
    print("남자")


num=[4,2,3,6,7,4,1]
if num[0]==1 or num[0]==3:
    print("남자")
else:
    print("여자")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for i in q3:
    if i == "정":
        continue
    print(i, end =' ')
print()

# 6번 리스트 컴프리헨션으로 풀기
q5 = [x for x in q3 if x != '정']
print(q5)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

for v in range(1,100,2):
    print(v,end=' ')
print()

for n in range(1,101):
    if n % 2 !=0:
        print(n, end=', ')

print()

w1 = [x for x in range(1,101) if x % 2 != 0]
print(w1, end= ', ')
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for n in q4:
    if len(n) >= 5:
        print(n, end=' ')

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for y in q5:
    if y.islower():
        print(y)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for w in q6:
    if w.islower():
        print(w.upper())
    else:
        print(w.lower())

#--------------------------------------------------------------------------------------

# 일반적인 방법

numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션

numbers2 = [x for x in range(1,101)]
print(numbers2)

x = [x for x in range(1,100) if True]