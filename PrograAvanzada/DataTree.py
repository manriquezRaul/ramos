class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeZ = TreeNode('Z')
nodeM = TreeNode('M')
nodeY = TreeNode('Y')
nodeW = TreeNode('W')
nodeN = TreeNode('N')
nodeF = TreeNode('F')
nodeX = TreeNode('X')
nodeT = TreeNode('T')
nodeO = TreeNode('O')
nodeP = TreeNode('P')
nodeS = TreeNode('S')
nodeQ = TreeNode('Q')

root.left = nodeZ
root.right = nodeM

nodeZ.left = nodeY
nodeZ.right = nodeW

nodeY.left = nodeX
nodeY.right = nodeT

nodeM.left = nodeN
nodeM.right = nodeF

nodeN.left = nodeO
nodeN.right = nodeP

nodeP.right = nodeQ

nodeF.right = nodeS

# Test
print("root.right.left.data:", root.right.left.data)