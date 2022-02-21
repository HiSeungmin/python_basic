
# Node 구현
from email import header
from os import link

# 다양한 링크드 리스트 구조 (더블 링크드 리스트 = 이중 연결 리스트)

class Node:
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init(self, data):
        self.head = Node(data)
        self.tail = self.head # 뒤부터 검색이 가능해야해서 tail

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next # 노드의 끝을 찾아가기 위해서
            new = Node(data)
            node.next = new # 새로운 노드에 가려고
            new.prev = node
            self.tail = new # 바뀐 마지막 노드를 tail로 설정

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next 


double_linked_list = NodeMgmt(0)
for data in range(1,10):
    double_linked_list.insert(data)
double_linked_list.desc()