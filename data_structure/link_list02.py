
# Node 구현
from email import header
from os import link

class NODE:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class NODE_Mgmt: # 링크드 리스트를 관리
    def __init__(self, data):
        self.head = NODE(data)    

    def add(self, data): # 맨 끝에 노드를 추가하는 함수
        if self.head == "":
            self.head = NODE(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = NODE(data)

    def desc(self): # 해당 링크드리스트 전체를 출력해주는 함수 (description)
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data): # 데이터 삭제하는 함수(head 삭제, 마지막 노드 삭제, 중간 노드 삭제)
        if self.head =="":
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:  # 중간, 마지막 노드 삭제
                if node.next.data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

                
# linkedlist1 = NODE_Mgmt(0)
# print(linkedlist1.desc())

# for data in range (1, 10):
#     linkedlist1.add(data)
# linkedlist1.desc()

linkedlist1 = NODE_Mgmt(0)
print(linkedlist1.desc())
print(linkedlist1.head)

# head를 지워봄
linkedlist1.delete(0)
print(linkedlist1.head)

for data in range(1,10):
    linkedlist1.add(data)

linkedlist1.desc()
linkedlist1.delete(4) # 중간 노드 지워보기
linkedlist1.desc()

linkedlist1.delete(8)
linkedlist1.desc()

linkedlist1.delte(9) # 마지막 노드 지워보기
linkedlist1.desc()

