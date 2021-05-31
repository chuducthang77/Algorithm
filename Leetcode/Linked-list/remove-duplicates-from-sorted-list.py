# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head        
        temp = head
        if head == None:
            return head
        while current.next != None:
            #Case 1: 2 adjacent nodes have equal value but there does not exist a next node
            if current.val == temp.val and temp.next == None:
                current.next = None
            #Case 2: 2 adjacent nodes have equal value but there exists a next node
            elif current.val == temp.val:
                temp = temp.next
            #Case 3: 2 adjacent nodes do not have equal value
            else:
                current.next = temp
                current = temp

#---------Test case-----------
arr = [1,1,1,2,4,5,5]
node = []
for i in range(len(arr)):
    node.append(ListNode(arr[i]))

for i in range(len(node)):
    if i < len(arr) - 1:
        node[i].next = node[i+1]

head = node[0]
while head != None:
    print(head.val)
    head = head.next

solution = Solution()
solution.deleteDuplicates(node[0])
print('----------------------------')

head = node[0]
while head != None:
    print(head.val)
    head = head.next
