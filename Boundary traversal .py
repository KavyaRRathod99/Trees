class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
  
def collectLeftBoundary(root, result):
    while root != None:
        if root.left == None and root.right == None:
            break
 
        result.append(root.data)
 
        if root.left != None:
            root = root.left 
        else:
            root = root.right
 
def collectLeafNodes(root, result):
    if root == None:
        return 
    if root.left == None and root.right == None:
        result.append(root.data)
        return
 
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)
 
def collectRightBoundaryInReverseDirection(root, result):
 
    temp = []
    while root != None:
        if root.left == None and root.right == None:
            break
 
        temp.append(root.data)
 
        if root.right != None:
            root = root.right 
        else:
            root = root.left
 
    temp = temp[::-1]
    for ele in temp:
        result.append(ele)
 
def printBoundaryTraversal(root):
    result = []
 
    result.append(root.data)
    # task-1: collect left boundary 
    collectLeftBoundary(root.left, result)
 
    # task-2: collect leaf nodes (in left to right direction)
    collectLeafNodes(root, result)
 
    # task-3: collect right boundary(in reverse direction)
    collectRightBoundaryInReverseDirection(root.right, result)
 
    print(*result)
 
root=TreeNode(11)
obj2 = TreeNode(7)
obj3 = TreeNode(5)
obj4 = TreeNode(3)
obj5 = TreeNode(9)
obj6 = TreeNode(8)
obj7 = TreeNode(10)
obj8 = TreeNode(15)
obj9 = TreeNode(13)
obj10 = TreeNode(12)
obj11 = TreeNode(14)
obj12 = TreeNode(20)
obj13 = TreeNode(18)
obj14 = TreeNode(25)

root.left = obj2 
root.right = obj8 
 
obj2.left = obj3 
obj2.right = obj5 
 
obj3.left = obj4 

obj2.left = obj3 
obj2.right = obj5 
 
obj5.left = obj6 
obj5.right = obj7 
 
obj8.left = obj9 
obj8.right = obj12 
 
obj9.left = obj10
obj9.right = obj11


obj12.left = obj13 
obj12.right= obj14



printBoundaryTraversal(root)
