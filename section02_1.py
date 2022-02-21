# Section02_1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello World!")
print("""Hello Python3!""")
print('''Hello python!!''')

print()

#Separator 옵션 사용
print('T','E','S','T', sep='')  #문자를 붙여서 출력(공백없이)
print('2019','02','19',sep='-') #문자 사이에 -를 넣어서 출력
print('niceman','google.com',sep='@')

#end 옵션 사용
print('Welcome To', end=' ') #다음 문장과 연결(줄바꿈을 하지 않음)
print('the black parade',end=' ')
print('piano notes')

print()

#format 사용 [] : 대괄호, {} : 중괄호, () : 소괄호
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You',b='Me'))
print()

#%s:문자, %d:정수, %f:실수
print("%s's favorite number is %d" % ('Eunki', 7)) 

print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price: {1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b:4.2f}".format(a=776, b=6534.123))

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n\n')
print('\t\ttest')

"""

참고 : Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\000 : 널 문자
...

"""