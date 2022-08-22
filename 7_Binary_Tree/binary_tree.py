class Queue(object):
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    if not self.is_empty():
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[-1].value

  def __len__(self):
    return self.size()

  def size(self):
    return len(self.items)




class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
    

class BinaryTree(object):
  def __init__(self, root):
        self.root = Node(root) 
    
  def insert(self, new_val):
        self.insert_helper(self.root, new_val)
  
  def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
             
  def search(self, find_val):
        return self.search_helper(self.root, find_val)
   
  def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
            
  def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal   

  def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal      
      
  def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
  def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
          
            
if __name__ == '__main__':
    tree = BinaryTree(15)
    tree.insert(12)
    tree.insert(7)
    tree.insert(14)
    tree.insert(27)
    tree.insert(20)
    tree.insert(23)
    tree.insert(88)     
    
    print(tree.preorder_print(tree.root, ""))
    print(tree.inorder_print(tree.root, ""))
    print(tree.postorder_print(tree.root, ""))
    print(tree.levelorder_print(tree.root))
      
