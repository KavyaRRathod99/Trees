class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
def printBottomViewOfBinaryTree(root):
    result = []
 
    Q = [[root, 0]]
    #Q = [[12, -1], [10, 3], [14, 2], [56, 10]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        # [address, hd] 
        node = currPair[0]
        hd = currPair[1]
        
        store[hd] = node.data
 
        # something to insert into our result 
        if hd not in store:
            store[hd] = node.data 
 
        if node.left != None:
            Q.append([node.left, hd - 1])
 
        if node.right != None:
            Q.append([node.right, hd + 1])
 
    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])
 
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

printBottomViewOfBinaryTree(root)
