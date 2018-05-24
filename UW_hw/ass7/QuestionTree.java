package ass7;

//Dibo Zhang
//CSE 143 BN
//Homework 7
//

import java.io.*;
import java.util.*;

public class QuestionTree {

    //
    private Scanner console = new Scanner(System.in);

    //
    private QuestionNode root;

    /*

    */
    QuestionTree() {
        root = new QuestionNode("computer");
    }

    /*

    */
    public void read(Scanner input) {
        root = read(input, root);
    }

    /*

    */
    private QuestionNode read(Scanner input, QuestionNode root) {
        if (input.nextLine().equals("Q:")) {
            root = new QuestionNode(input.nextLine());
            root.left = read(input, root.left);
            root.right = read(input, root.right);
        } else {
            root = new QuestionNode(input.nextLine());
        }
        return root;
    }

    /*

    */
    public void write(PrintStream output) {
        write(output, root);
    }

    /*

    */
    private void write(PrintStream output, QuestionNode root) {
        if (root != null) {
            if (root.left == null && root.right == null) {
                output.println("A:");
                output.println("" + root.data);

            } else {
                output.println("Q:");
                output.println("" + root.data);
                write(output, root.left);
                write(output, root.right);
            }
        }
    }

    /*

    */
    public void askQuestions() {
        this.root = askQuestions(root);
    }

    /*

    */
    private QuestionNode askQuestions(QuestionNode root) {
//        QuestionNode r = root;
        if (root.left == null && root.right == null) {
            boolean ans = yesTo("Would your object happen to be " + root.data + "?");
            if (ans) {
                System.out.println("Great, I got it right!");
            } else {
                System.out.print("What is the name of your object? ");
                String name = console.nextLine();
                String namePrev = root.data;
                System.out.println("Please give me a yes/no question that");
                System.out.println("distinguishes between your object");
                System.out.print("and mine--> ");
                String question = console.nextLine();
                ans = yesTo("And what is the answer for your object?");
                if (ans) {
                    root = new QuestionNode(question, new QuestionNode(name), new QuestionNode(namePrev));
//                    QuestionNode node = new QuestionNode(question, new QuestionNode(name), new QuestionNode(namePrev));
//                    if(root.data.equals("computer")){
//                        root = node;
//                    } else {
//                        root.left = node;
//                    }

//                    r.left = root;
//                    root = root.left;
                } else {
                    root = new QuestionNode(question, new QuestionNode(namePrev), new QuestionNode(name));
//                    QuestionNode node = new QuestionNode(question, new QuestionNode(namePrev), new QuestionNode(name));
//                    if(!root.data.equals("computer")){
//                        root = node;
//                    } else {
//                        root.right = node;
//                    }
//                    r.right = root;
//                    root = root.right;
                }
            }
            return root;
        } else {
            boolean ans = yesTo(root.data);
            if (ans) {
                root.left = askQuestions(root.left);
                return root;

            } else {
                root.right = askQuestions(root.right);
                return root;

            }
        }
//        return root;
    }

    // post: asks the user a question, forcing an answer of "y " or "n";
    //returns true if the answer was yes, returns false otherwise
    public boolean yesTo(String prompt) {
        System.out.print(prompt + " (y/n)? ");
        String response = console.nextLine().trim().toLowerCase();
        while (!response.equals("y") && !response.equals("n")) {
            System.out.println("Please answer y or n.");
            System.out.print(prompt + " (y/n)? ");
            response = console.nextLine().trim().toLowerCase();
        }
        return response.equals("y");
    }
}