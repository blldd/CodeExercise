import java.util.Arrays;

/**
 * Created by L on 2018/3/12.
 * 统计一个数字在排序数组中出现的次数。
 */
public class C12NumofK {
    public int GetNumberOfK(int [] array , int k) {
        int res = 0;
        int len = array.length;
        if(len == 0){
            return res;
        }

        int firstK = getFirst(array, k, 0, len-1);
        int lastK = getLast(array, k, 0, len-1);

        if(firstK != -1 && lastK!= -1){
            res = lastK - firstK +1;
        }
        return res;
    }

    //recursion
    private int getFirst(int[] array, int k, int start, int end) {
        if(start > end){
            return -1;
        }
        int mid = (start + end) >> 1;
        if(k < array[mid]){
            return getFirst(array, k, start, mid - 1);
        } else if(k > array[mid]){
            return getFirst(array, k, mid + 1, end);
        } else {                                                 //array[mid] == k
            if((mid == start) || (array[mid-1] != k)){
                return mid;
            } else{
                return getFirst(array, k, start, mid - 1);
            }
        }

    }

    //循环666
    private int getLast(int[] array, int k, int start, int end) {
        int len = array.length;
        int mid = (start + end) >> 1;
        while(start <= end){
            if(array[mid] > k){
                end = mid-1;
            }else if(array[mid] < k){
                start = mid+1;
            }else if(mid+1 < len && array[mid+1] == k){
                start = mid+1;
            }else{
                return mid;
            }
            mid = (start + end) >> 1;
        }
        return -1;
    }

    //666
    /*
    public:
    int GetNumberOfK(vector<int> data ,int k) {
        int lower = getLower(data,k);
        int upper = getUpper(data,k);

        return upper - lower + 1;
    }

    //获取k第一次出现的下标
    int getLower(vector<int> data,int k){
        int start = 0,end = data.size()-1;
        int mid = (start + end)/2;

        while(start <= end){
            if(data[mid] < k){
                start = mid + 1;
            }else{
                end = mid - 1;
            }
            mid = (start + end)/2;
        }
        return start;
    }
    //获取k最后一次出现的下标
    int getUpper(vector<int> data,int k){
         int start = 0,end = data.size()-1;
        int mid = (start + end)/2;

        while(start <= end){
            if(data[mid] <= k){
                start = mid + 1;
            }else{
                end = mid - 1;
            }
            mid = (start + end)/2;
        }

        return end;
    }
     */

    public static void main(String[] args){
        C12NumofK nk = new C12NumofK();
        int[] array = {6,-3,-2,7,-15,1,2,2};
        int k = 2;
        Arrays.sort(array);
        int res = nk.GetNumberOfK(array, k);
        System.out.println(res);
    }
}
