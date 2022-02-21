# Section07_1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 클래스 형태로 코딩하고 변수에 할당해서 인스턴스화시킴.
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
#class 클래스명:
#    함수
#    함수
#    함수

# 예제1
# 클래스 구성 : 속성(전화번호, 주소, ..), 메소드(먹다, 움직이다, ...)
class UserInfo:
    def __init__(self, name ): #클래스를 최초 초기화할 때 사용
        self.name = name
    def user_info_p(self):
        print("Name : ",self.name)
    
# 네임스페이스 (user1과 user2는 각각 다른 값을 가지고 있음)
# 인스턴스화된 변수들은 서로 독립적인 네임스페이스를 가지고 있음.
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제2 (Self의 이해)
class SelfTest():
    def function1():
        print('function1 called!')
    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
#self_test.function1() -> 오류, self가 없기 때문에
SelfTest.function1() # self가 없다면 클래스에서 직접 호출해야한다.
self_test.function2() # self가 있는 것은 인스턴스를 생성해서 호출하거나

print(id(self_test))
SelfTest.function2(self_test) # 클래스를 즉시 호출해서 인자로 넣어줘야 한다.

# 예제3
# 클래스 변수, 인스턴스 변수(self가 들어가야함)

class WareHouse:
    # 클래스 변수 (모두가 공유하기 때문에 모두 창고를 사용)
    # 예) 연봉 인상율 stock_num = 0.05
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self): # 인스턴스가 종료될 때 호출
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

del user1 

#print(user1.stock_num)
# 자기 네임스페이스에서 변수를 찾았는데 없으면 클래스에서 찾고 출력. 클래스에도 없으면 에러 발생.

print(user2.stock_num) # user1을 지웠기 때문에 __del__함수가 호출되어 stock_num-1이 됨.
print(user3.stock_num)