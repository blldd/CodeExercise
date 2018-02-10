import java.security.PublicKey;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by L on 2018/2/10.
 * 操作给定的二叉树，将其变换为源二叉树的镜像。
 */
public class B10MirrorTree {
    public static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }
    }

//recursion
    public void Mirror(TreeNode root) {
        if(root == null){
            return;
        }
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        if(root.left != null){
            Mirror(root.left);
        }
        if(root.right != null){
            Mirror(root.right);
        }
    }

    //非递归
//    public void Mirror(TreeNode root) {
//        if(root == null) return;
//        Stack<TreeNode> stack = new Stack<TreeNode>();
//        stack.push(root);
//        while(!stack.empty()) {
//            TreeNode node = stack.pop();
//            if(node.left != null || node.right != null) {
//                TreeNode nodeLeft = node.left;
//                TreeNode nodeRight = node.right;
//                node.left = nodeRight;
//                node.right = nodeLeft;
//            }
//            if(node.left != null) stack.push(node.left);
//            if(node.right != null) stack.push(node.right);
//        }
//    }

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

    //逐层遍历
    public static ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        ArrayList<Integer> res = new  ArrayList<Integer>();
        Queue<TreeNode> node =  new LinkedList<TreeNode>();    //Queue
        if(root == null){
            return res;
        }
        res.add(root.val);
        node.add(root);
        while(node.size()!=0){
            root = node.poll();
            if(root.left!=null){
                res.add(root.left.val);
                node.add(root.left);
            }
            if(root.right!=null){
                res.add(root.right.val);
                node.add(root.right);
            }
        }
        return res;
    }

    public static void main(String []args){
        B10MirrorTree mt = new B10MirrorTree();
        int []pre = {1,2,4,7,3,5,6,8};
        int []in = {4,7,2,1,5,3,8,6};
        TreeNode tree1 = reConstructBinaryTree(pre, in);
        ArrayList<Integer> a = PrintFromTopToBottom(tree1);
        System.out.println("层序遍历：");
        for(int i:a){
            System.out.print(i+" ");
        }
        System.out.println();

        mt.Mirror(tree1);

        ArrayList<Integer> b = PrintFromTopToBottom(tree1);
        System.out.println("镜像层序遍历：");
        for(int i:b){
            System.out.print(i+" ");
        }
        System.out.println();

    }
}
