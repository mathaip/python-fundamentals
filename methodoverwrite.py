class A:
	def __init__(self,a):

		self.value = a
	def printing(self):
		print("value=", self.value)
class B(A):
	def __init__(self,b,a):
		self.val = b
		super(). __init__(a)
	def printing(self):
		super().printing()
		print("Hello")
b = B(5,6)
b.printing()
print (b.val)
print (dir(b))


