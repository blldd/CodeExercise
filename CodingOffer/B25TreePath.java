import java.util.ArrayList;

/**
 * Created by L on 2018/2/25.
 * 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
 */
public class B25TreePath {

    public static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }

    }

    /**
     *
     * @param root
     * @param target
     * @return
     *
     */
    private ArrayList<ArrayList<Integer>> listAll = new ArrayList<ArrayList<Integer>>();
    private ArrayList<Integer> list = new ArrayList<Integer>();
    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
        if(root == null)
            return listAll;
        list.add(root.val);
        target -= root.val;
        if(target == 0 && root.left == null && root.right == null)
            listAll.add(new ArrayList<Integer>(list));
        FindPath(root.left, target);
        FindPath(root.right, target);
        list.remove(list.size()-1);
        return listAll;
    }

//    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root, int target) {
//        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
//        if(root == null){
//            return result;
//        }
//        ArrayList<Integer> array = new ArrayList<Integer>();
//        int sum = 0;
//        path(root, target, result, array, sum);
//        return result;
//    }
//
//    private void path(TreeNode root, int target, ArrayList<ArrayList<Integer>> result, ArrayList<Integer> array, int sum) {
//        if(root == null){
//            return;
//        }
//        sum += root.val;
//        if(root.left == null && root.right == null){
//            if(target == sum){
//                array.add(root.val);
//                result.add(new ArrayList<Integer>(array));
//                array.remove(array.size()-1);
//            }
//            return ;
//        }
//        array.add(root.val);
//        path(root.left, target, result, array, sum);
//        path(root.right, target, result, array, sum);
//        array.remove(array.size()-1);
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

    public static void main(String[] args){
        B25TreePath tp = new B25TreePath();
        int []pre = {1,2,4,7,3,5,6,8};
        int []in = {4,7,2,1,5,3,8,6};
        TreeNode root = reConstructBinaryTree(pre, in);
        int target = 14;
        ArrayList<ArrayList<Integer>> result = tp.FindPath(root, target);
        System.out.println(result.size());
        for(ArrayList<Integer> i:result){
            System.out.println(i.size());

            for(int j:i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
