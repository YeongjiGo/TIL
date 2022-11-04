from dataclasses import dataclass

class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""

        new_node = Node(data)
  
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "/"

        iterator = self.head

        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += f"{iterator.data}|"
            iterator = iterator.next
        
        return res_str

'''
# 데이터 2, 3, 5, 7, 11을 담는 노드를 생성

head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node # 반복자(이터레이터)

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
'''
# 링크드 리스트 실행해보기
# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 노드 순서대로 출력
iterator = my_list.head # 반복자(이터레이터)

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next