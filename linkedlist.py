class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist(Node):
	def __init__(self):
		self.head = None
	def add_node(self,new_date):
		new_node = Node(new_date)
		new_node.next = self.head
		self.head = new_node
	def printlist(self):
		temp=self.head
		print(temp.data,"----",temp.next)
		if(temp.next == None):
			print("none")
		else:
			temp=temp.next
		while(temp!= self.head):
			print(temp.data,"---",temp.next)
			temp=temp.next


linked = Linkedlist()
ch = 'y'
while (ch=='y'):
	inp= input("enter the data:")
	node = Node(inp)
	linked.add_node(node)
	ch = input ("Do you want to continue?")

linked.printlist()
