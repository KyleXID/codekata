# Day23.Week5(day5) Linked List : https://stackoverflow.com/c/wecode/questions/186

class Node:
  def __init__(self,data):
    self.data   = data
    self.next   = None
    # self.before = None

class MyLinkedList(object):

  def __init__(self):
    self.head = None

  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next
    print("End")

  def get(self, index):
    cur = self.head
    i   = 0

    while i != index:
      i += 1
      cur = cur.next

    if cur.data == None:
      return -1
    return cur.data

  def addAtHead(self, val):
    newhead = Node(val)

    temp = self.head

    self.head = newhead
    self.head.next = temp

  def addAtTail(self, val):
    newtail = Node(val)
    cur = self.head

    while cur.next != None:
      cur = cur.next

    cur.next = newtail

  def addAtIndex(self, index, val):
    cur = self.head
    i = 0

    if index == 0:
      self.addAtHead(val)

    while i != index-1:
      i += 1
      cur = cur.next

    if cur.next == None:
      self.addAtTail(val)
    else:
      new = Node(val)
      new.next = cur.next
      cur.next = new

  def deleteAtIndex(self, index):
      i   = 0
      cur = self.head
      if index == 0:
        self.head = self.head.next

      while i != index-1:
        i += 1
        cur = cur.next

      if cur == None:
        return -1

      cur.next = cur.next.next


linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
linkedList.deleteAtIndex(1)  # now the linked list is 1->3
linkedList.addAtHead(5)
linkedList.addAtTail(11)
linkedList.addAtIndex(3, 9)
linkedList.print_list()
print(linkedList.get(3),9)
linkedList.addAtHead(4)

#다른 로직
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def add(self, preNode, val):
        node = Node(val)
        node.pre = preNode
        node.next = preNode.next
        node.pre.next = node.next.pre = node
        self.size += 1

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1

    def forward(self, start, end, cur):
        while start != end:
            start += 1
            cur = cur.next
        return cur

    def backward(self, start, end, cur):
        while start != end:
            start -= 1
            cur = cur.pre
        return cur

    def get(self, index):
        if 0 <= index <= self.size // 2:
            return self.forward(0, index, self.head.next).val
        elif self.size // 2 < index < self.size:
            return self.backward(self.size - 1, index, self.tail.pre).val
        return -1

    def addAtHead(self, val):
        self.add(self.head, val)

    def addAtTail(self, val):
        self.add(self.tail.pre, val)

    def addAtIndex(self, index, val):
        if 0 <= index <= self.size // 2:
            self.add(self.forward(0, index, self.head.next).pre, val)
        elif self.size // 2 < index <= self.size:
            self.add(self.backward(self.size, index, self.tail).pre, val)

    def deleteAtIndex(self, index):
        if 0 <= index <= self.size // 2:
            self.remove(self.forward(0, index, self.head.next))
        elif self.size // 2 < index < self.size:
            self.remove(self.backward(self.size - 1, index, self.tail.pre))
