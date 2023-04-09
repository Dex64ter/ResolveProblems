class Node(object):
    def __init__(self, data= None, LeftChild= None, RightChild= None) -> None:
      self.data = data
      self.LeftChild = LeftChild
      self.RightChild = RightChild
    
    def search(self, value):
      if self.data == value:
        return True
      elif value < self.data and self.LeftChild:
        return self.LeftChild.search(value)
      elif value > self.data and self.RightChild:
        return self.RightChild.search(value)
      else:
        return False

    def insert(self, value):
      if self.data == value:
        return False
      elif value < self.data:
        if self.LeftChild:
          return self.LeftChild.insert(value)
        else:
          self.LeftChild = Node(value)
          return True
      else:
        if self.RightChild:
          return self.RightChild.insert(value)
        else:
          self.RightChild = Node(value)
          return True

    # def remove(self, value):
    #   if self == None:
    #     return False
      
    #   if self.data == value:
    #     if self.LeftChild is None and self.RightChild is None:
    #       self == None
    #       return True
    #     elif self.LeftChild and self.RightChild is None:
    #       self = self.LeftChild
    #       return True
    #     elif self.LeftChild is None and self.RightChild:
    #       self = self.RightChild
    #       return True
    #     else:
    #       moveNode = self.RightChild
    #       moveNodeParent = None
    #       while moveNode.LeftChild:
    #         moveNodeParent = moveNode

root = Node(1)
root.insert(10)
root.insert(5)
root.insert(12)
root.insert(8)
print(root.search(1))