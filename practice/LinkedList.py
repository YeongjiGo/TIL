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
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += f" {iterator.data} | "
            iterator = iterator.next
        
        return res_str

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator

    def find_node_with_data(self, data):
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
        
        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

        
    def insert_after(self, previous_node, data):
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = previous_node.next
        else: # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def delete_after(self, previous_node):
        """링크드 리스트 삭제. 주어진 노드 뒤 노드를 삭제한다."""
        data = previous_node.next.data

        # 지우려는 노드가 tail 노드일 때:
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        # 두 노드 사이 노드를 지울 때:
        else:
            previous_node.next = previous_node.next.next


        return data


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

# str 메소드 실행해보기
linked_list = LinkedList()

# 링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)
'''

'''
# 탐색 연산
# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 링크드 리스트 노드에 접근 (데이터 가지고 오기)
print(my_list.find_node_at(3).data)

# 링크드 리스트 노드에 접근 (데이터 바꾸기)
my_list.find_node_at(2).data = 13

print(my_list)
'''

'''
my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

node_2 = my_list.find_node_at(2) # 인덱스 2에 있는 노드 접근
my_list.insert_after(node_2, 6) # 인덱스 2 뒤에 6 삽입

print(my_list)

head_node = my_list.head # 헤드 노드 접근(헤드 노드는 인스턴스 변수이기 때문에 메소드를 안써도 가져올 수 있음)
my_list.insert_after(head_node, 9)

print(my_list)
'''

my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)
'''
node_2 = my_list.find_node_at(2) # 인덱스 2 노드 접근
my_list.delete_after(node_2) # 인덱스 2 뒤 데이터 삭제

print(my_list)

second_to_last_node = my_list.find_node_at(2) # 맨 끝에서 두 번째 노드 접근
print(my_list.delete_after(second_to_last_node)) # tail 노드 삭제

print(my_list)'''