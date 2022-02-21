# 재귀함수
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)

recursive(4)

# append, pop 메서드 사용
data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())

# pop, push 기능 구현
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1] # 리스트의 맨 끝 값
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(pop())
print(pop())
print(pop())