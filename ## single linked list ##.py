##   single linked list    ##

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None

  def insertatfirst(self,data):
    newnode=Node(data)
    newnode.next=self.head
    self.head=newnode

  def insertatend(self,data):
    newnode=Node(data)

    if self.head is None:
      self.head=newnode
      return
    temp=self.head
    while temp.next is not None:
      temp=temp.next
    temp.next=newnode

  def insertatrandom(self,data,pos):
    newnode=Node(data)

    if pos==1:
      self.insertatfirst(data)
      return
    temp=self.head
    for i in range(pos-2):
      temp=temp.next
    newnode.next=temp.next
    temp.next=newnode
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data,end=" -> ")
      temp=temp.next

  def deleteatfirst(self):
    if self.head is None:
         return "no linked list"

    self.head=self.head.next

  def deleteatlast(self):
    if self.head is None:
      return " empty"
    temp=self.head
    while temp.next.next is not None:
      temp=temp.next
    temp.next=None
  def deleteatrandom(self,pos):
    if pos==1:
      self.deleteatfirst()
      return
    newnode=Node(data)
    temp=self.head
    for i in range(pos-2):
      temp=temp.next
    temp.next=temp.next.next

  def search(self,key):
    if self.head is None:
      print("not found or empty\n")
      return
    temp=self.head
    while temp:
      if temp.data==key:
        print( "found\n")
        return
      temp=temp.next
    print( "not found\n")

  def reverse(self):
    prev=None
    curr=self.head
    temp=curr
    while curr:
      curr=curr.next
      temp.next=prev
      prev=temp
      temp=curr
    self.head=prev






l=LinkedList()
l.insertatfirst(5)
l.insertatfirst(4)
l.insertatfirst(3)
l.insertatfirst(2)
l.insertatfirst(1)
l.insertatrandom(6,3)
l.deleteatrandom(3)
l.deleteatrandom(1)
l.deleteatrandom(4)


l.display()



