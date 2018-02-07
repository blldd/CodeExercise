/**
 * Created by L on 2018/2/7.
 */
public class B07ReorderArray {
    public int [] reOrderArray(int [] array) {
        int length = array.length;
        int[] temp = new int[length];
        int j = 0;
        for(int i = 0; i < length; i++){
            if(array[i] % 2 == 1){
                temp[j] = array[i];
                j++;
            } else {
                continue;
            }
        }
        for(int i = 0; i < length; i++){
            if(array[i] % 2 == 0){
                temp[j] = array[i];
                j++;
            } else {
                continue;
            }
        }

        for(int i = 0; i < length; i++){
            array[i] = temp[i];
        }
        return array;
    }

//    swap
//public void reOrderArray(int [] array) {
//    for(int i= 0;i<array.length-1;i++){
//        for(int j=0;j<array.length-1-i;j++){
//            if(array[j]%2==0&&array[j+1]%2==1){
//                int t = array[j];
//                array[j]=array[j+1];
//                array[j+1]=t;
//            }
//        }
//    }
//}

    /*
整体思路：
首先统计奇数的个数
然后新建一个等长数组，设置两个指针，奇数指针从0开始，偶数指针从奇数个数的末尾开始 遍历，填数
*/
//public void reOrderArray(int [] array) {
//    if(array.length==0||array.length==1) return;
//    int oddCount=0,oddBegin=0;
//    int[] newArray=new int[array.length];
//    for(int i=0;i<array.length;i++){
//        if((array[i]&1)==1) oddCount++;
//    }
//    for(int i=0;i<array.length;i++){
//        if((array[i]&1)==1) newArray[oddBegin++]=array[i];
//        else newArray[oddCount++]=array[i];
//    }
//    for(int i=0;i<array.length;i++){
//        array[i]=newArray[i];
//    }
//}

    public static void main(String []args){
        B07ReorderArray ra = new B07ReorderArray();
        int[] array = {1,2,3,4,5,6,7,8};//1,3,5,7,2,4,6,8
        ra.reOrderArray(array);
        for(int i:array){
            System.out.print(i);
        }
        System.out.println();
    }
}
