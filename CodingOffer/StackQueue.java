import java.util.ArrayList;
import java.util.Stack;

/**
 * Created by L on 2018/1/30.
 */
public class StackQueue {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int node) {
        if(!stack2.isEmpty()){
            int temp = stack2.pop();
            stack1.push(temp);
        }
        stack1.push(node);
    }

    public int pop() {
        while(!stack1.isEmpty()){
            int temp = stack1.pop();
            stack2.push(temp);
        }
        int result = stack2.pop();
        return result;
    }

    public static void main(String []args){

        ArrayList<Integer> array = new ArrayList<Integer>();
        StackQueue sq = new StackQueue();
        sq.push(1);
        sq.push(2);
        sq.push(3);
        array.add(sq.pop());
        array.add(sq.pop());
        sq.push(4);
        array.add(sq.pop());
        sq.push(5);
        array.add(sq.pop());
        array.add(sq.pop());
        for(int a:array){
            System.out.print(a);
        }
        System.out.println();
    }
}
