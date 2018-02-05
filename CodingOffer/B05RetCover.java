/**
 * Created by L on 2018/2/5.
 */
public class B05RetCover {
    int rectCover(int target) {
        if(target<1){
            return 0;
        } else if(target==1){
            return 1;
        } else if(target==2){
            return 2;
        }else{
            return rectCover(target-1)+rectCover(target-2);
        }
    }
    public static void main(String []args){
        B05RetCover rc = new B05RetCover();
        int result = rc.rectCover(8);
        System.out.println(result);
    }
}
