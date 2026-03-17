class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    new_node = Node(data)

    if self.head == None: # 첫 노드가 아무것도 없으면 자기거 세팅
      self.head == new_node
      return
    
    current = self.head # 어펜드를 할 때 출발 포인트 세팅

    while current.next: # 마지막 노드찾기가면 탈출 
      current = current.next
    
    current.next = new_node # 마지막 노드.next 에 뉴노드 추가!
    

