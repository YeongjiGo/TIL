class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data) # 새로운 데이터를 저장하는 노드
        #링크드 리스트가 비어있는 경우

        if self.head is None:
            self.head= new_node
            self.tail= new_node
        else: #이미 데이터가 있을때
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def find_node_at(self, index):
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단 해당 노드가 없으면 None리턴"""
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            
            iterator = iterator.next
        return None
    
    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next

        return res_str
    def insert_after(self, previous_node, data):
        new_node = Node(data)

        if previous_node is self.tail: #끝에 추가
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else: #노드 사이에 삽입
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node
            

        
       
# 빈 링크드 리스트 정의
my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)
tail_node = my_list.tail
my_list.insert_after(tail_node, 5)
print(my_list)
print(my_list.tail.data)

tail_node_7 = my_list.find_node_at(3)
my_list.insert_after(tail_node_7, 3)
print(my_list)

tail_node_2 = my_list.find_node_at(2)
my_list.insert_after(tail_node_2, 2)
print(my_list)

