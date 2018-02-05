/**
 * Created by L on 2018/2/5.
 */
public class B05Jump {
    int jumpFloorII(int number) {
        int a=1,b=2,c=0;

        if(number <= 0) {
            return 0;
        }

        int[] array = new int[number+1];
        array[0] = 1;
        array[1] = 1;
        for(int i = 2; i <= number; i++){
            array[i] = 0;
            for(int j = 0; j < i; j++){
                array[i] += array[j];
            }
        }

        return array[number];
    }
    public static void main(String []args){
        B05Jump j = new B05Jump();

        int result = j.jumpFloorII(8);
        System.out.println(result);
    }
}
