import java.util.ArrayList;
import java.util.Stack;

/**
 * Created by L on 2018/1/29.
 */
public class LinkList {
    private static class ListNode {
        int val;
        ListNode next = null;
        ListNode(int val){
            this.val = val;
        }
    }

    public static ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<Integer> s = new Stack<Integer>();
        while(listNode != null){
            s.push(listNode.val);
            listNode = listNode.next;
        }
        while(!s.isEmpty()){
            result.add(s.pop());
        }
        return result;
    }

    public static void main(String []args){
        ListNode raw = new ListNode(0);
        ListNode head = raw;            //define head pointer
        for(int i = 1; i < 6; i++){
            ListNode newNode = new ListNode(i);
            raw.next = newNode;
            raw = newNode;
        }
//        ListNode node1=new ListNode(1);
//        ListNode node2=new ListNode(2);
//        ListNode node3=new ListNode(3);
//        ListNode node4=new ListNode(4);
//        ListNode node5=null;
//        ListNode node6=new ListNode(6);
//        node1.next=node2;
//        node2.next=node3;
//        node3.next=node4;
        ArrayList<Integer> result = printListFromTailToHead(head);
        System.out.println(result);

    }
}


/*//递归
    ArrayList<Integer> arrayList=new ArrayList<Integer>();
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        if(listNode!=null){
            this.printListFromTailToHead(listNode.next);
            arrayList.add(listNode.val);
        }
        return arrayList;
    }
    */