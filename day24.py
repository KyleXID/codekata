# Day24.Week6(day1) Reverse Linked List 링크드 리스트의 순서를 뒤집어서 반환하는 함수입니다.

def reverseList(head):
  cur = head
  before = None

  while cur != None:
    after = cur.next
    cur.next = before
    before = cur
    cur = after

  head = before

  return head

#다른 방법
def reverseList(head):
  newList = None

  while head != None:
    print(head.val)
    temp = head
    head = head.next
    temp.next = newList
    newList = temp

  return temp
