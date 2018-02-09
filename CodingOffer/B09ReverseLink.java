/**
 * Created by L on 2018/2/9.
 * 输入一个链表，反转链表后，输出链表的所有元素。
 */
public class B09ReverseLink {
    public static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode ReverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode pre = null;
        ListNode next = null;
        while(head != null){
            next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }

    public static void main(String []args){
        B09ReverseLink rl = new B09ReverseLink();
        ListNode node = new ListNode(0);
        ListNode head = node;
        for(int i = 1; i < 7;i++){
            ListNode newNode = new ListNode(i);
            node.next = newNode;
            node = newNode;
        }
        ListNode result = rl.ReverseList(head);
        while(result.next != null){
            System.out.print(result.val);
            result = result.next;
        }

    }
}
