package ass8;
//Dibo Zhang
//CSE 143 BN
//Homework 8
//
public class HuffmanNode implements Comparable<HuffmanNode>{
   public int data;
   public int frequency;
   public HuffmanNode left;
   public HuffmanNode right;
   
   //constructs 
   public HuffmanNode(int frequency) {
      this(frequency, null, null);
   }
   
   //
   public HuffmanNode(int frequency, HuffmanNode left, HuffmanNode right) {
      this.frequency = frequency;      //**not data
      this.left = left;
      this.right = right;
   }
   
   
   //
   public int compareTo(HuffmanNode other){
      return frequency - other.frequency;
   }
}