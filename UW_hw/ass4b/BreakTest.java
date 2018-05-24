package ass4b;

/**
 * Created by L on 2018/5/11.
 */
public class BreakTest {
    public static void main(String[] args){

        int cnt = 0;
        while (cnt<4) {
            System.out.println("cnt-->" + cnt);
            for (int i = 0; i < 4; i++) {
                if (i == 2) {
                    System.out.println("i-->" + i);
                    break;
                } else {
                    System.out.println("i-->" + i);
                    System.out.println("else");
                }
            }
            cnt ++;
        }
    }
}
