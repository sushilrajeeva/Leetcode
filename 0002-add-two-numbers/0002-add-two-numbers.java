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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        ListNode cur1 = l1;
        ListNode cur2 = l2;

        int carry = 0;

        while(cur1!=null && cur2!=null){

            if(cur1.val + cur2.val + carry > 9){
                cur1.val = cur1.val + cur2.val + carry - 10;
                carry = 1;
            }else{
                cur1.val = cur1.val + cur2.val + carry;
                carry = 0;
            }

            current.next = cur1;
            cur1 = cur1.next;
            cur2=cur2.next;
            current = current.next;

        }

        while(cur1!=null){
            
            if(cur1.val+carry>9){
                cur1.val = cur1.val + carry -10;
                carry = 1;
            }else{
                cur1.val = cur1.val + carry;
                carry = 0;
            }

            current.next = cur1;
            cur1 = cur1.next;
            current = current.next;

        }

        while(cur2!=null){

            if(cur2.val + carry > 9){
                cur2.val = cur2.val + carry - 10;
                carry = 1;
            }else{
                cur2.val = cur2.val + carry;
                carry = 0;
            }

            current.next = cur2;
            cur2 = cur2.next;
            current = current.next;

        }

        if(carry == 1){
            current.next = new ListNode(1);
        }

        return dummy.next;
        
    }
}