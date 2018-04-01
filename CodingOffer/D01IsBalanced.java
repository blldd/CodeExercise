import com.sun.xml.internal.bind.v2.model.core.ID;

/**
 * Created by L on 2018/4/1.
 */
public class D01IsBalanced {
    public static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }

    }

    public static TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        TreeNode root = reConstructBinaryTree(pre,0,pre.length-1,in,0,in.length-1);
        return root;
    }
    //前序遍历{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}
    private static TreeNode reConstructBinaryTree(int[] pre, int startPre, int endPre, int[] in, int startIn, int endIn) {
        if(startPre>endPre||startIn>endIn)
            return null;
        TreeNode root=new TreeNode(pre[startPre]);

        for(int i=startIn;i<=endIn;i++)
            if(in[i]==pre[startPre]){
                root.left=reConstructBinaryTree(pre,startPre+1,startPre+i-startIn,in,startIn,i-1);
                root.right=reConstructBinaryTree(pre,i-startIn+startPre+1,endPre,in,i+1,endIn);
                break;
            }
        return root;
    }

    public int TreeDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        int nLeft = TreeDepth(root.left);
        int nRight = TreeDepth(root.right);

        return nLeft > nRight?(nLeft+1):(nRight+1);
    }

    public boolean IsBalanced_Solution(TreeNode root) {
        if(root == null){
            return true;
        }
        int nLeft = TreeDepth(root.left);
        int nRight = TreeDepth(root.right);
        int diff = nRight - nLeft;
        if (diff > 1 || diff < -1) {
            return false;
        }
        return IsBalanced_Solution(root.left) && IsBalanced_Solution(root.right);
    }

    public static void main(String[] args){
        int []pre = {1,2,4,7,3,5,6,8};
        int []in = {4,7,2,1,5,3,8,6};
        TreeNode resultTree = reConstructBinaryTree(pre, in);
        D01IsBalanced ib = new D01IsBalanced();

        boolean result = ib.IsBalanced_Solution(resultTree);
        System.out.println(result);
    }
}
