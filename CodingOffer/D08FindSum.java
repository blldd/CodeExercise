import java.util.ArrayList;

/**
 * Created by L on 2018/4/8.
 * 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，
 * 如果有多对数字的和等于S，输出两个数的乘积最小的。
 */
public class D08FindSum {
    public ArrayList<Integer> FindNumbersWithSum(int [] array, int sum) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i = 0; i < array.length; i++){

            for(int j = i+1; j < array.length; j++){
                int temp = array[i];
                temp += array[j];
                if(temp == sum){
                    res.add(array[i]);
                    res.add(array[j]);
                    return res;
                }
            }

        }
        return res;
    }

    public static void main(String[] args){
        D08FindSum fs = new D08FindSum();
        int[] array = {1,2,3,4,5,6,7,8};
        int sum = 9;
        ArrayList<Integer> res = fs.FindNumbersWithSum(array, sum);
        for(int i:res){
            System.out.print(i+" ");
        }
    }
}
