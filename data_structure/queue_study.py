import queue
from this import d

# FIFO
data_queue = queue.Queue() 

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print()

# LIFO
d_queue = queue.LifoQueue()
d_queue.put("wow")
d_queue.put(7)

print(d_queue.qsize())
print(d_queue.get())

# PriorityQueue

dt_queue = queue.PriorityQueue()
dt_queue.put((10,"Korea")) # 튜플로 넣음, 첫 번째는 우선순위를 나타냄
dt_queue.put((5, 1))
dt_queue.put((15,"China"))

print(dt_queue.qsize()) # 데이터는 3개, 우선순위는 1번이 제일 높은 것임. 
print(dt_queue.get())
print(dt_queue.get())
print()

# enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))
print(dequeue())
print(dequeue())
print(dequeue())
print()

# LIFO, FIFO, enqueue, dequeue 구현해보기

# FIFO
fifo = queue.Queue()

fifo.put("hi")
fifo.put("hello")
fifo.put("nice")

print(fifo.qsize())
print(fifo.get())

# LIFO
lifo = queue.LifoQueue()

lifo.put("hi")
lifo.put("hello")
lifo.put("nice")

print(lifo.qsize())
print(lifo.get())

# enqueue, dequeue 함수 만들기

q_list = list()

def en(value):
    q_list.append(value)

def de():
    value = q_list[0]
    del q_list[0]
    return value

for i in range(10):
    en(i)

print(len(q_list))
print(de())
print(de())