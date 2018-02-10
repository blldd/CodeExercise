/**
 * Created by L on 2018/2/10.
 * 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构
 */
public class B10SubTree {
    public static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }
    }
    /*思路：参考剑指offer
    1、首先设置标志位result = false，因为一旦匹配成功result就设为true，
    剩下的代码不会执行，如果匹配不成功，默认返回false
    2、递归思想，如果根节点相同则递归调用DoesTree1HaveTree2（），
    如果根节点不相同，则判断tree1的左子树和tree2是否相同，
    再判断右子树和tree2是否相同
    3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，
    DoesTree1HasTree2中，如果Tree2为空，则说明第二棵树遍历完了，即匹配成功，
    tree1为空有两种情况（1）如果tree1为空&&tree2不为空说明不匹配，
    （2）如果tree1为空，tree2为空，说明匹配。
    */
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        boolean result = false;
        if(root1 != null && root2 != null){
            if(root1.val == root2.val){
                result = tree1HasTree2(root1, root2);
            }
            if(!result){
                result = HasSubtree(root1.left, root2);
            }
            if(!result){
                result = HasSubtree(root1.right, root2);
            }
        }
        return result;
    }

    private boolean tree1HasTree2(TreeNode root1, TreeNode root2) {
        if(root1 == null && root2 != null) {
            return false;
        } else if (root2 == null){
            return true;
        }
        if(root1.val != root2.val){
            return false;
        }
        return tree1HasTree2(root1.left, root2.left) && tree1HasTree2(root1.right, root2.right);
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
        int []pre1 = {1,2,4,7};
        int []in1 = {4,7,2,1};
        TreeNode tree2 = reConstructBinaryTree(pre1, in1);
        B10SubTree st = new B10SubTree();

        boolean result = st.HasSubtree(tree1, tree2);
        System.out.println(result);
    }
}
