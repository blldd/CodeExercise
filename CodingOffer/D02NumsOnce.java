/**
 * Created by L on 2018/4/2.
 * 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
 */
public class D02NumsOnce {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        if(array.length < 2)
            return ;
        int myxor = 0;
        int flag = 1;
        for(int i = 0 ; i < array.length; ++ i )
            myxor ^= array[i];
        while((myxor & flag) == 0)
            flag <<= 1;
        for(int i = 0; i < array.length; ++ i ){
            if((flag & array[i]) == 0)
                num2[0]^= array[i];                 //
            else
                num1[0]^= array[i];
        }
    }

    public static void main(String[] args){
        int []array = {1,2,4,7,3,5,6,8};
        int []num1 = {4,7,2,1,5,3,8,6};
        int[] num2 = {2,3,4,2,3,5};
        D02NumsOnce no = new D02NumsOnce();
        no.FindNumsAppearOnce(array, num1, num2);
        System.out.println(num1[0]);
    }
}
