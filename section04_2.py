# Section04_2
# 문자열, 문자열 연산, 슬라이싱

str1 = "I AM GIRL."
str2 = 'NiceWoman'
str3 = '' #공백은 글자수:0
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 ="Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\t Tab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
""" 
문자열 
멀티라인 
테스트 
"""
print(multi)
print()
#문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "NiceMan"

print(str_o1*100) # 곱하기는 반복으로 100번 반복한다는 의미
print(str_o2+str_o3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77))
print(str(10.4))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

# print(a.islower()) # a는 소문자니?
# print(b.endswith('e')) # b는 'e'로 끝나니?
# print(a.capitalize()) # 첫글자를 대문자로
# print(a.replace('nice', 'good')) # 'nice'를 'good'으로
# print(list(reversed(b))) # 거꾸로 list로 출력
# print()

# 전체 주석 : ctrl+/

a = 'niceman' 
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:])
print(b[0:4:2]) # 0부터 4까지 2칸 뛰어서
print(b[1:-2]) # -1:'e', -2:'g' 그래서 1인 r부터 'g'까지
print(b[::-1]) # 처음과 끝이 지정되지 않고 -1번째 부터

