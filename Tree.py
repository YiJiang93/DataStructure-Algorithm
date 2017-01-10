#102
def levelOrder(self, root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	res = []
	if root == None:
		return res
	q = [root]
	while len(q) != 0:
		res.append([node.val for node in q])
		new_q = []
		for node in q:
			if node.left:
				new_q.append(node.left)
			if node.right:
				new_q.append(node.right)
		q = new_q
	return res

#107
def levelOrderBottom(self, root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	stack = [(root, 0)]
	res = []
	while stack:
		node, level = stack.pop()
		if node:
			if len(res) < level+1:
				res.insert(0, [])
			res[-(level+1)].append(node.val)
			stack.append((node.right, level+1))
			stack.append((node.left, level+1))
	return res
#404
def sumOfLeftLeaves(self, root):
	"""
	:type root: TreeNode
	:rtype: int
	"""
	if not root:
		return 0
	s=[root]
	res=0
	tmp=root
	while s:
		tmp=s.pop()
		if tmp.left:
			s.append(tmp.left)
			if not tmp.left.left and not tmp.left.right:
				res+=tmp.left.val
		if tmp.right:
			s.append(tmp.right)
	return res
#110
def isBalanced(self, root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	if not root:
		return True
	if abs(self.height(root.left)-self.height(root.right))<=1:
		return self.isBalanced(root.left) and self.isBalanced(root.right)
	else:
		return False

def height(self,root):
	if not root:
		return 0
	return max(self.height(root.left),self.height(root.right))+1
	
#257
def binaryTreePaths(self, root):
	res=[]	
	if not root:
		return res
	s=str(root.val)
	self.dfs(root,s,res)
	return res
	
def dfs(self,root,s,res):
	if not root.left and not root.right:
		res.append(s)
	if root.left:
		self.dfs(root.left,s+"->"+str(root.left.val),res)
	if root.right:
		self.dfs(root.right,s+"->"+str(root.right.val),res)
		
#112
def hasPathSum(self, root, sum):
	"""
	:type root: TreeNode
	:type sum: int
	:rtype: bool
	"""
	if not root:
		return False
	num=root.val
	res=[]
	self.dfs(root,num,res)
	for e in res:
		if e==sum:
			return True
	return False
	

def dfs(self,root,num,res):
	if not root.left and not root.right:
		res.append(num)
	if root.left:
		self.dfs(root.left,num+root.left.val,res)
	if root.right:
		return self.dfs(root.right,num+root.right.val,res)
		
#101
def isSymmetric(self, root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	if not root:
		return True
	else:
		return self.symmetric(root.left,root.right)



def symmetric(self,left,right):
	if not left and not right:
		return True
	if not right or not left:
		return False
	if right.val==left.val:
		outs=self.symmetric(right.right,left.left)
		ins=self.symmetric(right.left,left.right)
		return outs and ins
	return False
#235
def lowestCommonAncestor(self, root, p, q):
	"""
	:type root: TreeNode
	:type p: TreeNode
	:type q: TreeNode
	:rtype: TreeNode
	"""
	while root:
		if p.val<root.val and q.val <root.val:
			root=root.left
		elif p.val>root.val and q.val>root.val:
			root=root.right
		else:
			return root