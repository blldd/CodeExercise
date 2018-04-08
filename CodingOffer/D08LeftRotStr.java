/**
 * Created by L on 2018/4/8.
 * 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
 * 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
 * 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
 */
public class D08LeftRotStr {
    public String LeftRotateString(String str,int n) {
        String res = "";
        if(str.length() == 0){
            return res;
        }
        n %= str.length();
        StringBuffer sb = new StringBuffer();
        sb.append(str.substring(n, str.length()));
        sb.append(str.substring(0, n));
        res = sb.toString();
        return res;
    }

    public static void main(String[] args){
        D08LeftRotStr lrs = new D08LeftRotStr();
        String str = "";
        int n = 2;
        String res = lrs.LeftRotateString(str, n);
        System.out.println(res);
    }
}
