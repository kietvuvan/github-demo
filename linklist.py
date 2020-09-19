class Node:
	def __init__(self,carge=None,next=None):
		self.carge=carge
		self.next=next
	def __str__(self):
		return str(self.carge)

node=Node("hello")
print(node)
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next=node2
node2.next=node3
def print_list(node):
	while node is not None:
		print(node,end=" ")
		node=node.next
#print_list(node2)
def print_backword(list):
	if list is None:
		return
	head=list
	tail=list.next
	print_backword(tail)
	print(head,end=" ")
#print_backword(node1)
def remove_list(list):
	if list is None:
		return
	head=list
	second=list.next
	head.next=second.next
	second.next=None
	return second
print(remove_list(node1))
print_list(node1)


 




