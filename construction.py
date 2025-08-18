class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self,value):
         new_node=Node(value)
         self.head=new_node
         self.tail=new_node
         self.length=1
         
    def printlist(self):
        temp=self.head
        while temp is not None:
           print(temp.value)
           temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
          self.head=new_node
          self.tail=new_node
        else:
          self.tail.next=new_node
          self.tail=new_node
          self.length=self.length+1
        return True
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
         self.head=new_node
         self.tail=new_node
        else:
          new_node.next=self.head
          self.head=new_node

          def get(self,index):
             if index<0 or index>=self.length:
                return None
        temp=self.head
        for __ in range (self,index):
          temp=temp.next
          return temp
        def insert(self,index,value):
            if index<0 or index>self.length:
               return False
            if index==0:
              self.prepend()
            return True
            if index==self.length:
               self.append=(value)
            return True
            new_node=Node(value)
        



object= Linkedlist(2)
object.append(7)
object.append(5)
object.prepend(6)
object.printlist()




   

        