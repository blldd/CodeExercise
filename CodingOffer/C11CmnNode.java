import java.util.List;

/**
 * Created by L on 2018/3/11.
 * 输入两个链表，找出它们的第一个公共结点。
 */
public class C11CmnNode {

    public static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }
/*
//别人的方法：运用HasnMap的特性

    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        ListNode current1 = pHead1;
        ListNode current2 = pHead2;


        HashMap<ListNode, Integer> hashMap = new HashMap<ListNode, Integer>();
        while (current1 != null) {
            hashMap.put(current1, null);
            current1 = current1.next;
        }
        while (current2 != null) {
            if (hashMap.containsKey(current2))
                return current2;
            current2 = current2.next;
        }

        return null;

    }
 */
    public ListNode FindFirstCommonNode(ListNode current1, ListNode current2) {
        ListNode pHead1 = current1;// 链表1
        ListNode pHead2 = current2;// 链表2
        if(current1 == null || current2 == null){
            return null;
        }
        int cnt1 = 1;
        while(current1.next != null){
            current1 = current1.next;
            cnt1++;
        }
        int cnt2 = 1;
        while(current2.next != null){
            current2 = current2.next;
            cnt2++;
        }
        int cnt = cnt1 - cnt2;
        if(cnt >= 0){
            while(cnt > 0){
                pHead1 = pHead1.next;
                cnt --;
            }
        } else if(cnt < 0){
            while (cnt < 0){
                pHead2 = pHead2.next;
                cnt ++;
            }
        }

        while(pHead1 != null && pHead2 != null && pHead1!= pHead2){
            pHead1 = pHead1.next;
            pHead2 = pHead2.next;
        }

        return pHead1;
    }

    public static void main(String[] args){
        C11CmnNode cn = new C11CmnNode();

        ListNode node = new ListNode(0);
        ListNode pHead1 = node;
        for(int i = 1; i < 7;i++){
            ListNode newNode = new ListNode(i);
            node.next = newNode;
            node = newNode;
        }
        ListNode node1 = new ListNode(1);
        ListNode pHead2 = node1;
        for(int i = 2; i < 7; i++){
            ListNode newNode = new ListNode(i);
            node1.next = newNode;
            node1 = newNode;
        }
        ListNode res = cn.FindFirstCommonNode(pHead1,pHead2);
        System.out.println(res.val);
    }
}
