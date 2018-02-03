/**
 * Created by L on 2018/1/31.
 */
public class A31RotateArray {
    public int minNumberInRotateArray(int [] array) {
        int low = 0;
        int high = array.length-1;
        while(low < high){
            int mid = (low + high) / 2;
            if(array[mid] > array[high]){
                low = mid + 1;
            } else if(array[mid] == array[high]){
                high = high - 1;
            } else {
                high = mid;
            }
        }
        return array[low];
    }

    public static void main(String []args){
        int [] array = {8,9,5,6,7};
        A31RotateArray ra = new A31RotateArray();
        int result = ra.minNumberInRotateArray(array);
        System.out.println(result);
    }
}
