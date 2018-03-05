import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

/**
 * Created by L on 2018/3/5.
 * 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
 * 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
 */
public class C05Half {
/*
    public int MoreThanHalfNum_Solution(int [] array) {
        int result = 0;
//        Map<Integer, Integer> map = new Map<Integer, Integer>();
        ArrayList<Integer> al = new ArrayList<Integer>();
        for(int i = 0; i < array.length; i++){
            if(al.contains(array[i])){
                al.indexOf(array[i]);
            }
        }

        return result;
    }
*/
    public int MoreThanHalfNum_Solution(int [] array) {
        int len=array.length;
        if(len<1){
            return 0;
        }
        int count=0;
        Arrays.sort(array);
        int num=array[len/2];
        for(int i=0;i<len;i++){
            if(num==array[i])
                count++;
        }
        if(count<=(len/2)){
            num=0;
        }
        return num;
    }

    /*//精彩
        int MoreThanHalfNum_Solution(vector<int> numbers) {
        int n = numbers.size();
        if (n == 0) return 0;

        int num = numbers[0], count = 1;
        for (int i = 1; i < n; i++) {
            if (numbers[i] == num) count++;
            else count--;
            if (count == 0) {
                num = numbers[i];
                count = 1;
            }
        }
        // Verifying
        count = 0;
        for (int i = 0; i < n; i++) {
            if (numbers[i] == num) count++;
        }
        if (count * 2 > n) return num;
        return 0;
    }
     */
    public static void main(String[] args){
        C05Half h = new C05Half();
//        int[] array = {1,2,3,2,2,2,5,4,2};
        int[] array = {2, 2, 3, 4};
        int result = h.MoreThanHalfNum_Solution(array);
        System.out.println(result);
    }
}
