class Solution:
    def deleteNode(self, node):
        next= node.next
        node.next=next.next
        node.val=next.val