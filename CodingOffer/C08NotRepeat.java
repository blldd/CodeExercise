import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;

/**
 * Created by L on 2018/3/8.
 * 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
 */
public class C08NotRepeat {

    public int FirstNotRepeatingChar(String str) {
        int res = -1;

        if(str.length() < 1 || str.length() >10000){
            return res;
        }
        List<Character> charList = new ArrayList<Character>();
        for(int i = 0; i < str.length(); i++){
            char ch = str.charAt(i);
            if(!charList.contains(ch)){
                charList.add(Character.valueOf(ch));
            } else {
                charList.remove(Character.valueOf(ch));
            }
        }
//        String[] strArr = str.split("");
//        ArrayList<String> strList = new ArrayList<String>();
//        for(String s : strArr){
//            strList.add(s);
//        }
//        HashSet<String> hs = new HashSet<String>(strList);
//        strList.clear();
//        strList.addAll(hs);
//        for(String s : strList){
//            System.out.println(s);
//        }
        if(charList.size()<1){
            return res;
        }
        char tmp = charList.get(0);
        res = str.indexOf(tmp);
        return res;
    }

    public int FirstNotRepeatingChar1(String str) {
        LinkedHashMap<Character, Integer> map = new LinkedHashMap<Character, Integer>();
        for(int i=0;i<str.length();i++){
            if(map.containsKey(str.charAt(i))){
                int time = map.get(str.charAt(i));
                map.put(str.charAt(i), ++time);
            }
            else {
                map.put(str.charAt(i), 1);
            }
        }
        int pos = -1;
        int i=0;
        for(;i<str.length();i++){
            char c = str.charAt(i);
            if (map.get(c) == 1) {
                return i;
            }
        }
        return pos;
    }


    public static void main(String[] args){
        C08NotRepeat np = new C08NotRepeat();
        String str = "googgle";
        int result = np.FirstNotRepeatingChar1(str);
        System.out.println(result);
    }
}
