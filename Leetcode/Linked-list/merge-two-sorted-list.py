# Definition for singly-linked list.
#TODO: Finish this problem
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current1 = l1
        current2 = l2
        result = ListNode()
        temp = result

        while current1 != None or current2 != None:
            
            if current1 == None and current2 != None:
                temp.next = current2
            elif current2 == None and current1 != None:
                temp.next = current1
            elif current1.val <= current2.val:
                tempNode = ListNode(current1.val)
                temp.next = tempNode
                current1 = current1.next
            else:
                tempNode = ListNode(current2.val)
                temp.next = tempNode
                current2 = current2.next

        result = result.next
        return result
        
#---------Test case-----------
arr = [1,2,4]
arr1 = [1,2,3]
node = []
node1 = []

for i in range(len(arr)):
    node.append(ListNode(arr[i]))
for i in range(len(arr1)):
    node1.append(ListNode(arr1[i]))

for i in range(len(node)):
    if i < len(arr) - 1:
        node[i].next = node[i+1]
for i in range(len(node1)):
    if i < len(arr1) - 1:
        node1[i].next = node1[i+1]

solution = Solution()
result = solution.mergeTwoLists(node[0], node1[0])
print(result)