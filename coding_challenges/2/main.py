def test_for_solution():
    solution = Solution()
    merged_list = solution.mergeTwoLists([1,2,4],[1,3,4])
    assert merged_list == [1,1,2,3,4,4]
    merged_list = solution.mergeTwoLists([],[])
    assert merged_list == []
    
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next
        
        
if __name__ == "__main__":
    test_for_solution()
    print("All tests passed")