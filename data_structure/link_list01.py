
# Node 구현
from email import header
from os import link

# class Node:
#     def __init__(self, data): # 인자가 하나인데 주소값을 넣어주려면 두 개의 인자를 받아와야한다.
#         self.data = data
#         self.next = None

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next # 다음 주소를 넣는 변수

def add(data):
    node = head
    while node.next: # 노드의 next값이 있으면! 즉 다음 데이터가 있다는 뜻
        node = node.next # 마지막 노드를 찾기 위해서
    node.next = Node(data) # 마지막 노드의 next는 None인 상태인데 여기에 새로운 노드 객체를 생성을 하면 전체 링크드 리스트에 새로운 노드를 연결한 것이 됨

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# head = node1 # 가장 앞에 있는 데이터 주소를 알아야함.

node1 = Node(1) # 맨 처음의 노드를 만든다. 맨 앞의 노드 값은 1
head = node1  # 그 노드를 head에 저장

for index in range(2, 11):
    add(index)

node = head
while node.next:
   print(node.data)
   node = node.next
print(node.data)
print()

# 데이터 사이에 데이터 추가하기
node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next # 주소값 바꾸기
node.next = node3
node3.next = node_next

node = head
while node.next:
   print(node.data)
   node = node.next
print(node.data)
