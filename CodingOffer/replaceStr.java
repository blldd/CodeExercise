/**
 * Created by L on 2018/1/29.
 */
public class replaceStr {
    public String replaceSpace(StringBuffer str) {
        if(str == null){
            return null;
        }
        StringBuffer result = new StringBuffer();
        for(int i = 0; i < str.length(); i++){
//            System.out.println(str.charAt(i));
            if(str.charAt(i) == ' '){
                result.append("%20");
            } else {
                result.append(str.charAt(i));
            }
        }
        return result.toString();
    }

    public static void main(String []args){
        replaceStr r = new replaceStr();
        StringBuffer rawStr = new StringBuffer("We Are Happy");
        String result = r.replaceSpace(rawStr);
        System.out.println(result);
    }
}
