class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None
class Linkedliat:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1  
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _in range (index):
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
        



            
          
        