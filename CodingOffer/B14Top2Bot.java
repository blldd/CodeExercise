import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by L on 2018/2/14.
 */
public class B14Top2Bot {
    public static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }

    }

    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        if(root == null){
            return res;
        }
        q.add(root);
        res.add(root.val);
        while(!q.isEmpty()){
            root = q.poll();
            if(root.left != null){
                res.add(root.left.val);
                q.add(root.left);
            }
            if(root.right != null){
                res.add(root.right.val);
                q.add(root.right);
            }
        }

        return res;
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

    public static void main(String []args){
        int []pre = {1,2,4,7,3,5,6,8};
        int []in = {4,7,2,1,5,3,8,6};
        TreeNode tree1 = reConstructBinaryTree(pre, in);

        B14Top2Bot tb = new B14Top2Bot();
        ArrayList<Integer> result = tb.PrintFromTopToBottom(tree1);
        for(int i:result){
            System.out.print(i+" ");
        }
    }
}
