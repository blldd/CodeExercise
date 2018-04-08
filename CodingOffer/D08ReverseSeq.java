import java.util.ArrayList;

/**
 * Created by L on 2018/4/8.
 * 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
 * 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。
 * 后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
 * Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
 */
public class D08ReverseSeq {
    public String ReverseSentence(String str) {
        String res = "";
        String[] array = str.split(" ");
        StringBuffer sb = new StringBuffer();
        if(array.length == 0){
            return str;
        }
        for(int i = array.length; i > 1; i--){
            sb.append(array[i-1]);
            sb.append(" ");
        }
        sb.append(array[0]);
        res = sb.toString();
        return res;
    }
    public static void main(String[] args){
        D08ReverseSeq rs = new D08ReverseSeq();
        String str = " ";
        String res = rs.ReverseSentence(str);
        System.out.println(res);
    }
}
