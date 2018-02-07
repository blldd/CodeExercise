/**
 * Created by L on 2018/2/7.
 */
public class B07Power {
    public double Power(double base, int exponent) {
        //由于exponent是int类型的整数，则可能包含正整数、0以及负整数三种情况。
        double temp=1;
        if(exponent>0){
            for(int i=1;i<=exponent;i++){
                temp=temp*base;
                if(temp>1.7976931348623157E308){
                    System.out.println("已经超出double类型的取值范围。");
                    return -1;
                }
            }
            return temp;

        }if(exponent<0){
            exponent=-exponent;
            for(int i=1;i<=exponent;i++){
                temp=temp*base;
                if(temp>1.7976931348623157E308){
                    System.out.println("已经超出double类型的取值范围。");
                    return -1;
                }
            }
            temp=1.0/temp;
            return temp;
        }else{
            return 1;
        }
    }

    //recursion
//    public double Power(double base, int exponent) {
//        int n=Math.abs(exponent);
//        if(n==0)
//            return 1;
//        if(n==1)
//            return base;
//        double  result=Power(base,n>>1);
//        result*=result;
//        if((n&1)==1)
//            result*=base;
//        if(exponent<0)
//            result=1/result;
//        return result;
//    }

    public static void main(String []args){
        B07Power p = new B07Power();
        double result = p.Power(8, 2);
        System.out.println(result);
    }
}
