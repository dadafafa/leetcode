/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
public RandomListNode copyRandomList(RandomListNode head) {
    RandomListNode curr = head;
    while (curr != null) {
        RandomListNode next = curr.next;
        RandomListNode copy = new RandomListNode(curr.label);
        curr.next = copy;
        copy.next = next;
        curr = next;
    }
    
    curr = head;
    while (curr != null) {
        curr.next.random = (curr.random != null) ? curr.random.next : null;
        curr = curr.next.next;
    }
    
    curr = head;
    RandomListNode headCopy = (curr != null) ? curr.next : null; 
    while (curr != null) {
        RandomListNode copy = curr.next;
        curr.next = copy.next;
        curr = curr.next;
        copy.next = (curr != null) ? curr.next : null;
    }
    return headCopy;
}
}




