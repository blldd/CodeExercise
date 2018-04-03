import java.util.ArrayList;

/**
 * Created by L on 2018/4/3.
 * 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
 * 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
 * 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
 * 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
 */
public class D03CotnusSeq {

    //awful
    public ArrayList<ArrayList<Integer>> FindContinuousSequence1(int sum) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

        if(sum == 1){
            return res;
        }

        int start = 0;
        if(sum/2%2 == 0){
            start = sum/2 -1;
        } else {
            start = sum/2;
        }
        for(int i = start; i > 2; i -= 2){
            ArrayList<Integer> array = new ArrayList<Integer>();
            if(sum%i == 0){
                int mid = sum/i;
                if(mid < (i/2) || mid*i!=sum){
                    continue;
                }
                for(int j = mid - (i/2); j <= mid + (i/2); j++){
                    array.add(j);
                }
            }
            if(array.size()>0){
                res.add(array);
            }
        }
        if(sum % 2 == 1){
            int small = sum/2;
            ArrayList<Integer> array = new ArrayList<Integer>();
            array.add(small);
            array.add(small+1);
            res.add(array);
        }
        return res;
    }

    //我寫的臭代碼
    public static ArrayList<ArrayList<Integer>> getSeq(int small, int big, int mid, int sum,ArrayList<ArrayList<Integer>> res){

        if(big == small){
            return res;
        }
        int tmp = (small + big) * (big - small + 1) / 2;

        if (tmp == sum) {
            ArrayList<Integer> array = new ArrayList<Integer>();
            for (int i = small; i <= big; i++) {
                array.add(i);
            }
            res.add(array);
            if(small<mid){
                getSeq(small+1, big+1, mid, sum, res);
            }
        } else if (tmp > sum) {
            getSeq(small+1, big, mid, sum, res);
        } else {
            getSeq(small, big+1, mid, sum, res);
        }
        return res;
    }

    public ArrayList<ArrayList<Integer>> FindContinuousSequence2(int sum) {

        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        int small = 1;
        int big = 2;
        if(sum < 3){
            return res;
        }
        int mid = (1+sum)/2;
        res = getSeq(small, big, mid, sum, res);

        return res;
    }

    //別人家的
    public ArrayList<ArrayList<Integer>> FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> lists=new ArrayList<ArrayList<Integer>>();
        if(sum<=1){return lists;}
        int small=1;
        int big=2;
        while(small!=(1+sum)/2){          //当small==(1+sum)/2的时候停止
            int curSum=(small + big) * (big - small + 1) / 2;
            if(curSum==sum){
                ArrayList<Integer> list=new ArrayList<Integer>();
                for(int i=small;i<=big;i++){
                    list.add(i);
                }
                lists.add(list);
                small++;big++;
            }else if(curSum<sum){
                big++;
            }else{
                small++;
            }
        }
        return lists;
    }


    public static void main(String[] args){
        D03CotnusSeq cs = new D03CotnusSeq();
        ArrayList<ArrayList<Integer>> res = cs.FindContinuousSequence2(3);
//        System.out.println(res.size());
        for (ArrayList<Integer> array:res) {
            for (Integer i:array) {
                System.out.print(i+" ");
            }
            System.out.println();
        }
    }
}
