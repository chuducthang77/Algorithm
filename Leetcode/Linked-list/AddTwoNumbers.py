#Instructions: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.

from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1Length = 0
        l2Length = 0
        result = ListNode()

        #Calculate the longer linked list for traversal
        temp = l1
        while temp != None:
            temp = temp.next
            l1Length += 1
        
        temp = l2
        while temp != None:
            temp = temp.next
            l2Length += 1

        #if length 1 is longer than length 2, then traverse on length 1 
        #create a remainder variable to remember the calculation greater than 0
        remainder = 0
        tempL1 = l1
        tempL2 = l2
        tempResult = result
        while tempL1 != None and tempL2 != None:
            #Check the remainder from the previous node
            total = 0
            if remainder == 0:
                total = tempL1.val + tempL2.val
            else:
                total = tempL1.val + tempL2.val + 1
                remainder = 0

            #Update the remainder
            if total > 9:
                total = total % 10
                remainder = 1

            tempSum = ListNode(total)

            #Create a result linked list to the next item
            tempResult.next = tempSum

            #Update to the next node
            tempResult = tempResult.next
            tempL1 = tempL1.next
            tempL2 = tempL2.next
        
        #In case one of two length is longer 
        if l1Length > l2Length:
            while tempL1 != None:
                total = 0
                if remainder == 0:
                    total = tempL1.val
                else:
                    total = tempL1.val + 1
                    remainder = 0

                #Update the remainder
                if total > 9:
                    total = total % 10
                    remainder = 1

                tempSum = ListNode(total)

                #Create a result linked list to the next item
                tempResult.next = tempSum

                #Update to the next node
                tempResult = tempResult.next
                tempL1 = tempL1.next
        else:
            while tempL2 != None:
                total = 0
                if remainder == 0:
                    total = tempL2.val
                else:
                    total = tempL2.val + 1
                    remainder = 0

                #Update the remainder
                if total > 9:
                    total = total % 10
                    remainder = 1

                tempSum = ListNode(total)

                #Create a result linked list to the next item
                tempResult.next = tempSum

                #Update to the next node
                tempResult = tempResult.next
                tempL2 = tempL2.next

        #In case of the remainder is still remaining
        if remainder != 0:
            tempNode = ListNode(1)
            tempResult.next = tempNode

        return result.next
#-------Main: Test case--------
#Test case: [1] [9], [1,1][9]

arr1 = [9,9,9,9,9,9,9]
arr2 = [9,9,9,9]
nodeArr1 = []
nodeArr2 = []
for number in arr1:
    tempNode = ListNode(number)
    nodeArr1.append(tempNode)

for number in arr2:
    tempNode = ListNode(number)
    nodeArr2.append(tempNode)

for i in range(len(nodeArr1)):
    if i < len(nodeArr1) - 1:
        nodeArr1[i].next = nodeArr1[i + 1]
 
for i in range(len(nodeArr2)):
    if i < len(nodeArr2) - 1:
        nodeArr2[i].next = nodeArr2[i + 1]

solution = Solution()
sol = solution.addTwoNumbers(nodeArr1[0], nodeArr2[0])

while sol != None:
    print(sol.val)
    sol = sol.next