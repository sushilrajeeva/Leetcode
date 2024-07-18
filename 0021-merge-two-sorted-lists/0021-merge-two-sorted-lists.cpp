/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* dummy = new ListNode(-1);
        ListNode* current = dummy;

        ListNode* cur1 = list1;
        ListNode* cur2 = list2;

        while(cur1!=NULL && cur2!=NULL){
            if(cur1->val<=cur2->val){
                ListNode* temp = cur1;
                cur1 = cur1->next;
                temp->next = NULL;
                current->next = temp;
            }else{
                ListNode* temp = cur2;
                cur2 = cur2->next;
                temp->next = NULL;
                current->next = temp;
            }
            current = current->next;
        }

        if(cur1!=NULL){
            current->next = cur1;
        }

        if(cur2!=NULL){
            current->next = cur2;
        }

        return dummy->next;
        
    }
};