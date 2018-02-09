/**
 * Created by L on 2018/2/9.
 * 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
 */
public class B09MergeLink {
    public static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }
    //recursion
//    public ListNode Merge(ListNode list1,ListNode list2) {
//        if(list1 == null){
//            return list2;
//        }
//        if(list2 == null){
//            return list1;
//        }
//        if(list1.val <= list2.val){
//            list1.next = Merge(list1.next, list2);
//            return list1;
//        }else{
//            list2.next = Merge(list1, list2.next);
//            return list2;
//        }
//    }

    public ListNode Merge(ListNode list1,ListNode list2) {
        if(list1==null){
            return list2;
        }
        if(list2==null){
            return list1;
        }

        ListNode pMergeHead = null;
        ListNode pCurrent = null;
        while(list1 != null && list2 != null){
            if(list1.val <= list2.val){
                if(pMergeHead == null){
                    pMergeHead = pCurrent = list1;
                } else {
                    pCurrent.next = list1;
                    pCurrent = pCurrent.next;
                }
                list1 = list1.next;
            } else {
                if(pMergeHead == null){
                    pMergeHead = pCurrent = list2;
                } else {
                    pCurrent.next = list2;
                    pCurrent = pCurrent.next;
                }
                list2 = list2.next;
            }
        }
        if(list1.next == null){
            pCurrent.next = list2;
        } else {
            pCurrent.next = list1;
        }

        return pMergeHead;
    }

    public static void main(String []args){
        B09MergeLink ml = new B09MergeLink();
        ListNode node = new ListNode(1);
        ListNode head0 = node;
        for(int i = 3; i < 10; i+=2){
            ListNode newNode = new ListNode(i);
            node.next = newNode;
            node = newNode;
        }
        ListNode node1 = new ListNode(0);
        ListNode head1 = node1;
        for(int i = 2; i < 10; i+=2){
            ListNode newNode = new ListNode(i);
            node1.next = newNode;
            node1 = newNode;
        }

        ListNode result = ml.Merge(head0, head1);
        while(result.next != null){
            System.out.print(result.val);
            result = result.next;
        }

    }
}
