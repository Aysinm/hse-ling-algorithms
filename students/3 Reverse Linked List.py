#Задание 3 (2 балла) разворачивание односвязного списка
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    def __str__(self):
        return str(self.val)

def print_backward(data):
    if data == None:
        return
    head = data
    tail = data.next
    print_backward(tail)
    print (head)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
print_backward(node2)
