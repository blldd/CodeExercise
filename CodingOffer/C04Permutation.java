import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

/**
 * Created by L on 2018/3/4.
 * 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
 * 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
 */
public class C04Permutation {

    public ArrayList<String> PermutationStr(String inputStr) {
        int len = inputStr.length();
        ArrayList<String> resArray = new ArrayList<String>();

        if(len == 1){
            resArray.add(inputStr);
        } else {
            for(int i = 0; i < len; i++){
                String tmp = inputStr.substring(0, i) + inputStr.substring(i+1, len);
                ArrayList<String> rawArray = PermutationStr(tmp);            //recursion
                ArrayList<String> tmpArray = PermutationStr(tmp);
                //
                for(String s : rawArray){
                    tmpArray.add(inputStr.substring(i, i+1) + s);
                }
                for(String s : tmpArray){
                    resArray.add(s);
                }
            }
        }
        return resArray;
    }


    public ArrayList<String> Permutation(String inputStr) {
        ArrayList<String> result = new ArrayList<String>();
        ArrayList<String> resArray = PermutationStr(inputStr);
        for (String s : resArray) {
            if (s.length() == inputStr.length()) {                   //去除递归产生的中间str
                result.add(s);
            }
        }

        HashSet hs = new HashSet(result);                            //aa   hash去重
        result.clear();
        result.addAll(hs);

        Collections.sort(result);                                    //排序
        return result;
    }




    /*
    public ArrayList Permutation(String str) {
        ArrayList res = new ArrayList();
        if (str != null && str.length() > 0) {
            PermutationHelper(str.toCharArray(), 0, res);
            Collections.sort(res);
        }
        return res;
    }
    public void PermutationHelper(char[] cs, int i, ArrayList list) {
        if(i == cs.length - 1) {
            String val = String.valueOf(cs);
            if (!list.contains(val))
                list.add(val);
        } else {
            for(int j = i; j < cs.length; ++j) {
                swap(cs, i, j);
                PermutationHelper(cs, i + 1, list);
                swap(cs, i, j);
            }
        }
    }
     */
    public static void main(String[] args){
        C04Permutation p = new C04Permutation();
        String inputStr = "aa";
        ArrayList<String> result = p.Permutation(inputStr);

        for(String outStr: result){
            System.out.println(outStr);
        }
    }
}
