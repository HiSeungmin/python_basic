# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello ", world)

hello("Python!")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!")
print(str)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1),val1, val2, val3)


# 예제3-1(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] #리스트[]로 반환 가능, 튜플()도 가능

lt = func_mul2(100)
print(lt, type(lt))

# 예제4
# *args, *kwargs

#def args_func(*args): #매개변수가 몇 개 넘어올지 모를 때 사용. *이 한 개라 투플 형태로 넘어옴.
#    print(type(args),args)

#def args_func(*args): 
#    for t in args:
#        print(t)

def args_func(*args): 
    for i,v in enumerate(args): #인덱스를 생성해서 출력됨.
        print(i,v)
#   for i,v in enumerate(range(10)):
#       print(i,v)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee') 

# kwargs (키워드)
def kwargs_func(**kwargs):  # *이 두개면 딕셔너리
#    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1='Kim', name2='Park', name3='Lee')


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs): # 가변인자 사용(필수는 아니라서 arg1, arg2 입력받아도 됨)
    print(arg1, arg2, args, kwargs)

example_mul(10,20)
example_mul(10,20,'park','kim', age1=24, age2=35)


# 예제5
# 중첩함수(클로저)
# '파이썬 데코레이터 클로저' 검색해보기
def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num+10000)

nested_func(10000) 

# 예제6 (hint)
def func_mul3(x : int) -> list:  # x는 int를 받고 list로 변환이 된다는 것을 알려줌.
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] 

print(func_mul3(5)) # 5.0을 넣어도 오류가 발생하지는 않음.

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int ) -> int:
    return num * 10

var_func = mul_10 # 변수에 할당
print(type(var_func),var_func)
print(var_func(10))


lambda_mul_10 = lambda x : x * 10 # 일반적인 함수보다 매우 간결. num과 x는 같은 것.
print('>>>',lambda_mul_10(10))

def func_final(x, y, func):
    print( x * y * func(10))

func_final(10,10,lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000)) #즉시 람다식을 사용할 수 있음.



