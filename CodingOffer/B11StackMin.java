import java.util.Iterator;
import java.util.Stack;

/**
 * Created by L on 2018/2/11.
 * 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
 */
public class B11StackMin {
    Stack<Integer> stack = new Stack<Integer>();
    public void push(int node) {
        stack.push(node);
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int min() {
        int min = top();
        int temp = 0;

        Iterator<Integer> iterator = stack.iterator();
        while(iterator.hasNext()){
            temp = iterator.next();
            if(temp < min){
                min = temp;
            }
        }
//        if(!stack.empty()){
//            min = top();
//            pop();
//            while(!stack.empty()){
//                int temp = top();
//                if(temp < min){
//                    min = temp;
//                }
//                pop();
//            }
//        }
        return min;
    }

    public static void main(String []args){
        B11StackMin sm = new B11StackMin();
        for(int i = 7; i < 10; i++){
            sm.stack.push(i);
        }
        int result = sm.min();
        for(int i = 5; i < 10; i++){
            sm.stack.push(i);
        }
        int result1 = sm.min();
        System.out.println(result);
        System.out.println(result1);
    }
}
