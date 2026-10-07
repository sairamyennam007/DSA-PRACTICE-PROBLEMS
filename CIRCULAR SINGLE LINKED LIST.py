##  circular linked list   ###




class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class CircularLinkedList:
  def __init__(self):
    self.head=None

  def insertatfirst(self,data):
    newnode=Node(data)
    if self.head is None:
       newnode.next=self.head
       self.head=newnode
       return

    temp=self.head
    while temp.next is not self.head:
      temp=temp.next
    newnode.next=self.head
    self.head=newnode
    temp.next=self.head

  def insertatlast(self,data):
    newnode=Node(data)

    if self.head is None:
      self.head=newnode
      newnode.next=self.head
      return
    temp=self.head
    while temp.next is not self.head:
      temp=temp.next
    temp.next=newnode
    newnode.next=self.head

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
  

  def deleteatfirst(self):
    if self.head is None:
         return "no linked list"
    
    temp=self.head
    while temp.next is not self.head:
      temp=temp.next
    self.head=self.head.next
    temp.next=self.head

  def deleteatlast(self):
    if self.head is None:
      return " empty"
    temp=self.head
    while temp.next.next is not self.head:
      temp=temp.next
    temp.next=self.head
  def deleteatrandom(self,pos):
    if pos==1:
      self.deleteatfirst()
      return
    temp=self.head
    for i in range(pos-2):
      temp=temp.next
    temp.next=temp.next.next

  def search(self,key):
    if self.head is None:
      print("not found or empty\n")
      return 
    temp=self.head
    while True:
      if temp.data==key:
        print( "found\n")
        return
      temp=temp.next
      if temp is self.head:
         print( "not found\n")
         break
    print("not found")

   

  

  def display(self):
    temp=self.head
    while True:
      print(temp.data,end=" -> ")
      temp=temp.next
      if temp is self.head:
        break






l=CircularLinkedList()# Create a single linked list of n numbers
l.insertatlast(1)
l.insertatlast(2)
l.insertatlast(3)
l.insertatlast(4)
l.insertatlast(5)
l.insertatfirst(0)



l.display()




