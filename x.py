class BST:
	def __init__(self,key):
		self.key = key
		self.lchild = None
		self.rchild = None

	def insert(self,data):
		if self.key == None:
			self.key = data
			return

		if self.key == data:
			return

		if self.key > data:
			if self.lchild:
				self.lchild.insert(data)
			else:
				self.lchild = BST(data)
		elif self.key < data:
			if self.rchild:
				self.rchild.insert(data)
			else:
				self.rchild = BST(data)


	def search(self,x):
		if self.key == x:
			print("found")

		else:
			if self.key > x:
				if self.lchild:
					self.lchild.search(x)
				else:
					print("Not Found")

			else:
				if self.rchild:
					self.rchild.search(x)
				else:
					print("Not Found")

	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key)
		if self.rchild:
			self.rchild.inorder()


	def delete(self,x):
		if self.key == None:
			print("No tree")
			return
		if self.key > x:
			if self.lchild:
				self.lchild = self.lchild.delete(x)
			else:
				print("No tree")
		elif self.key < x:
			if self.rchild:
				self.rchild = self.rchild.delete(x)
			else:
				print("No tree")

		else:
			if self.lchild is None:
				temp = self.rchild
				self = None
				return temp
			if self.rchild is None:
				temp = self.lchild
				self = None
				return temp
			n = self.lchild
			while n.rchild is not None:
				n = n.rchild
			self.key = n.key
			self.lchild = self.lchild.delete(n.key)
		return self


tree = BST(50)
tree.insert(30)
tree.insert(70)
tree.insert(40)
tree.insert(60)
tree.inorder()
tree.delete(50)
tree.inorder()


