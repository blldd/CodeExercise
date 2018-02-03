import java.util.ArrayList;

/**
 * Created by L on 2018/1/31.
 */
public class A31Fibnacci {
    public int Fibonacci(int n) {
        //array version
        ArrayList<Integer> array = new ArrayList<Integer>();
        array.add(0, 0);
        array.add(1, 1);
        for(int i = 2; i <= n; i++){
            array.add(i, array.get(i-2) + array.get(i-1));
        }
        //recursion version
//        int result = 0;
//        if(n == 0){
//            return 0;
//        } else if(n == 1){
//            return 1;
//        } else {
//            result = Fibonacci(n-2) + Fibonacci(n-1);
//        }
        return array.get(n);
    }

    //
    public int FibonacciBest(int n) {
        int a=1,b=1,c=0;
        if(n<0){
            return 0;
        }else if(n==1||n==2){
            return 1;
        }else{
            for (int i=3;i<=n;i++){
                c=a+b;
                b=a;
                a=c;
            }
            return c;
        }
    }
    public static void main(String []args){
        A31Fibnacci f = new A31Fibnacci();

        int result = f.Fibonacci(3);
        System.out.println(result);
    }
}
