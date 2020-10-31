/*
一个快指针，一个慢指针，快指针一次走两步，慢指针一次走一步，如果循环过程中快指针追上了慢指针，说明有环。如果跳出循环了，则说明没有环。
*/
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: True if it has a cycle, or false
     */
    public boolean hasCycle(ListNode head) {
        if(head == null || head.next == null){
            return false;
        }
        ListNode slow = head;
        ListNode fast = head;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow.val == fast.val){
                return true;
            }
        }
        return false;
    }
}
