# Section08
# 파이썬 모둘과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex 1 : ", Fibonacci.fib2(400))
print("ex 1 : ", Fibonacci().title)


# 사용2 <- 메모리를 많이 차지하기 때문에 권장하지 않음.
from pkg.fibonacci import* # 전체 다 가져오겠다!, 필요없는 것들도 전부 가져옴

Fibonacci.fib(500)

print("ex 2 : ", Fibonacci.fib2(600))
print("ex 2 : ", Fibonacci().title)


# 사용3(클래스) <- 권장하는 방법
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex 2 : ", fb.fib2(1600))
print("ex 2 : ", fb().title)


# 사용4(함수)
import pkg.calculations as c

print("ex 4 :", c.add(10,100))
print("ex 4 :", c.mul(10,100))


# 사용5(함수)
from pkg.calculations import div as d

print("ex 5 : ",int(d(100,10)))

#사용6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))

