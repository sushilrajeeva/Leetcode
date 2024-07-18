/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        ListNode cur1 = list1;
        ListNode cur2 = list2;

        while(cur1!=null && cur2!=null){
            if(cur1.val<=cur2.val){
                ListNode temp = cur1;
                cur1 = cur1.next;
                temp.next = null;
                current.next = temp;
            }else{
                ListNode temp = cur2;
                cur2 = cur2.next;
                temp.next = null;
                current.next = temp;
            }
            current = current.next;
        }

        if(cur1!=null){
            current.next = cur1;
        }

        if(cur2!=null){
            current.next = cur2;
        }

        return dummy.next;
        
    }
}