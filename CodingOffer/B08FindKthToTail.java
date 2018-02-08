import javax.swing.*;

/**
 * Created by L on 2018/2/8.
 * 输入一个链表，输出该链表中倒数第k个结点。
 */
public class B08FindKthToTail {
    public static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    //pre指针先跑，并且记录节点数，当pre指针跑了k-1个节点后，post指针开始跑，
    //当pre指针跑到最后时，post所指指针就是倒数第k个节点
    public ListNode FindKthToTail(ListNode head,int k) {
        ListNode pre = null, post = null;
        pre = head;
        post = head;
        int num = k;
        int count = 0;
        while(pre != null){
            pre = pre.next;
            count++;
            if(k<1){
                post = post.next;
            }
            k--;
        }
        if(count<num){
            return null;
        }
        return post;
    }

    public static void main(String []args){
        B08FindKthToTail ftt = new B08FindKthToTail();
        ListNode node = new ListNode(1);
        ListNode head = node;
        for(int i = 2; i < 7; i++){
            ListNode newNode = new ListNode(i);
            node.next = newNode;
            node = newNode;
        }
        ListNode result = ftt.FindKthToTail(head, 3);
        System.out.println(result.val);
    }
}
