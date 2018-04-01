import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by L on 2018/4/1.
 */
public class D01TreeDepth {

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

    //recursion
    public int D01TreeDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        int nLeft = D01TreeDepth(root.left);
        int nRight = D01TreeDepth(root.right);

        return nLeft > nRight?(nLeft+1):(nRight+1);
    }

    public int TreeDepth(TreeNode pRoot)
    {
        if(pRoot == null){
            return 0;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(pRoot);
        int depth = 0, count = 0, nextCount = 1;
        while(queue.size()!=0){
            TreeNode top = queue.poll();
            count++;
            if(top.left != null){
                queue.add(top.left);
            }
            if(top.right != null){
                queue.add(top.right);
            }
            if(count == nextCount){
                nextCount = queue.size();
                count = 0;
                depth++;
            }
        }
        return depth;
    }

    public static void main(String[] args){
        int result = 2;
        int []pre = {1,2,4,7,3,5,6,8};
        int []in = {4,7,2,1,5,3,8,6};
        TreeNode resultTree = reConstructBinaryTree(pre, in);
        D01TreeDepth tp = new D01TreeDepth();
        result = tp.TreeDepth(resultTree);
        System.out.println(result);
    }
}
