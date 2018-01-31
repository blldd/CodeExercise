import javax.swing.tree.TreeNode;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by L on 2018/1/29.
 */
public class BiTree {
    public static class TreeNode{
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
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

    //逐层遍历
    public static ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        ArrayList<Integer> res = new  ArrayList<Integer>();
        Queue<TreeNode> node =  new LinkedList<TreeNode>();
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

    //前序遍历
    public static void preOut(TreeNode tree){
        //stack
        Stack<Integer> stack = new Stack<Integer>();
        stack = preOut(tree, stack);
        System.out.println("前续遍历结果1：");
        while(!stack.isEmpty()){
            System.out.print(stack.pop() + " ");
        }
        System.out.println();

        //array
        ArrayList<Integer> array = new ArrayList<Integer>();
        array = preOutArray(tree, array);
        System.out.println("前续遍历结果2：");
        for(int a : array){
            System.out.print(a + " ");
        }
        System.out.println();
    }

    private static ArrayList<Integer> preOutArray(TreeNode tree, ArrayList<Integer> array) {
        if(tree == null){
            return null;
        }
        array.add(tree.val);
        if(tree.left != null){
            preOutArray(tree.left, array);
        }
        if(tree.right != null){
            preOutArray(tree.right, array);
        }
        return array;
    }

    private static Stack<Integer> preOut(TreeNode tree, Stack<Integer> stack) {
        if(tree == null){
            return null;
        }
        if(tree.right != null){
            preOut(tree.right, stack);
        }
        if(tree.left != null){
            preOut(tree.left, stack);
        }
        stack.push(tree.val);
        return stack;
    }

    //前序遍历
    public static void inOut(TreeNode tree){
        Stack<Integer> stack = new Stack<Integer>();
        stack = inOut(tree, stack);
        System.out.println("中续遍历结果：");
        while(!stack.isEmpty()){
            System.out.print(stack.pop() + " ");
        }
        System.out.println();
    }

    private static Stack<Integer> inOut(TreeNode tree, Stack<Integer> stack) {
        if(tree == null){
            return null;
        }
        if(tree.right != null){
            inOut(tree.right, stack);
        }
        stack.push(tree.val);
        if(tree.left != null){
            inOut(tree.left, stack);
        }
        return stack;
    }

    //后续遍历
    public static void postOut(TreeNode tree){
        Stack<Integer> stack = new Stack<Integer>();
        stack = postOut(tree, stack);
        System.out.println("后续遍历结果：");
        while(!stack.isEmpty()){
            System.out.print(stack.pop() + " ");
        }
        System.out.println();
    }

    private static Stack<Integer> postOut(TreeNode tree, Stack<Integer> stack) {
        if(tree == null){
            return null;
        }
        stack.push(tree.val);
        if(tree.right != null){
            postOut(tree.right, stack);
        }
        if(tree.left != null){
            postOut(tree.left, stack);
        }
        return stack;
    }

    public static void main(String []args){
        int []pre = {1,2,4,7,3,5,6,8};
        int []in = {4,7,2,1,5,3,8,6};
        TreeNode resultTree = reConstructBinaryTree(pre, in);
        preOut(resultTree);
        inOut(resultTree);
        postOut(resultTree);
        ArrayList<Integer> a = PrintFromTopToBottom(resultTree);
        System.out.println("层序遍历：");
        for(int i:a){
            System.out.print(i+" ");
        }
    }
}


/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
