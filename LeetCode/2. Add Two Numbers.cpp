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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3 = new ListNode();
        ListNode* start = l3;
        int ones = 0, carry = 0, sum = 0;
        
        while(l1 != nullptr || l2 != nullptr) {
            if (l1==nullptr) {
                l1 = new ListNode(0, nullptr);
            }
            if (l2==nullptr) {
                l2 = new ListNode(0, nullptr);
            }
            
            sum = l1->val + l2->val + carry;
            
            ones = int(sum % 10);
            carry = int(sum / 10);
            
            l3->val = ones;
            
            l1 = l1->next;
            l2 = l2->next;
            
            if (l1 || l2 || carry == 1) {
                l3->next = new ListNode();
                l3 = l3->next;
            }
        }
        
        if(carry == 1) {
            l3->val = 1;
        }
        
        return(start);
    }
};