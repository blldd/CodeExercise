package ass8;
//Dibo Zhang
//CSE 143 BN
//Homework 8
//

import java.io.*;
import java.util.*;

public class HuffmanTree {

    //
    private HuffmanNode root;
    //
    private boolean end;

    /*

    */
    HuffmanTree(int[] count) {
        Queue<HuffmanNode> q = new PriorityQueue<HuffmanNode>();
        HuffmanNode current;
        for (int i = 0; i < count.length; i++) {
            if (count[i] != 0) {
                current = new HuffmanNode(count[i]);
                current.data = i;
                q.add(current);
            }
        }
        current = new HuffmanNode(1);
        current.data = 256;
        q.add(current);
        while (q.size() > 1) {
            HuffmanNode node1 = q.remove();
            HuffmanNode node2 = q.remove();
            current = new HuffmanNode(node1.frequency + node2.frequency,
                    node1, node2);
            q.add(current);
        }
        root = q.remove();
    }

    /*

    */
    public void write(PrintStream output) {
        write(output, root, "");
    }

    /*

    */
    private void write(PrintStream output, HuffmanNode root, String num) {
        if (root.left == null && root.right == null) {
            output.println(root.data);
            output.println(num);
        } else {
            write(output, root.left, num + "0");
            write(output, root.right, num + "1");
        }
    }

    /*

    */
    HuffmanTree(Scanner input) {
        int n;
        String code;
        this.root = new HuffmanNode(0);         //***new root node
        for (this.end = true; input.hasNext(); this.root = this.reconstructTree(this.root, n, code)) {
            n = Integer.parseInt(input.nextLine());
            code = input.nextLine();
        }

//        end = true;
//        while (input.hasNext()) {
//            int n = Integer.parseInt(input.nextLine());
//            String code = input.nextLine();
//            root = reconstructTree(root, n, code);
//        }
    }

    /*

    */
    private HuffmanNode reconstructTree(HuffmanNode root, int n, String code) {
        if (code.equals("")) {
            root = new HuffmanNode(0);
            root.data = n;
        } else if (code.charAt(0) == '0') {
            if (root.left == null) {
                root.left = new HuffmanNode(0);
            }
            root.left = reconstructTree(root.left, n, code.substring(1));
        } else {
            if (root.right == null) {
                root.right = new HuffmanNode(0);
            }
            root.right = reconstructTree(root.right, n, code.substring(1));
        }
        return root;
    }

    /*

    */
    public void decode(BitInputStream input, PrintStream output, int eof) {
        while (end) {
            decode(root, input, output, eof);
        }
    }

    /*

    */
    private void decode(HuffmanNode root, BitInputStream input, PrintStream output, int eof) {
        if (root.left == null && root.right == null) {      // check leaf first***
            if (root.data == eof) {
                end = false;
            } else {
                output.write(root.data);
            }
        } else {                                            // else do down
            int readBit = input.readBit();                  // read bit first
            if (readBit == 0) {                             // check if 0 or 1
                decode(root.left, input, output, eof);
            } else {
                decode(root.right, input, output, eof);
            }
        }
    }
}