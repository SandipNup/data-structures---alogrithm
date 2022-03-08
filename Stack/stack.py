# stack implementation using singly linked list
class Node:
    """
        Class to create the node of the linked list
    """
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
     
    def __init__(self):
        """
            Head is set to none by default
        """
        self.head = None
     
    def is_empty(self):
        """
            Check if the stack is empty
        """
        if self.head == None:
            return True
        else:
            return False
     
    def push(self,data):
        """
        Adds data to the stack 
        """
         
        if self.head == None:
            self.head=Node(data)
             
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
     
    def pop(self):
        """
        Remove element from the head of the stack
        """
         
        if self.is_empty():
            return None
             
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data
     
    def peek(self):
        "Returns the element that is at the top of the stack"
         
        if self.is_empty():
            return None
             
        else:
            return self.head.data
     
         
stack_obj = Stack()
 
stack_obj.push(23)
stack_obj.push(28)
stack_obj.push(29)
  
print("\nElement at the top of stack is ",stack_obj.peek())
 
stack_obj.pop()
stack_obj.pop()
 
 
print("\nElement at the top of the stack is ", stack_obj.peek())