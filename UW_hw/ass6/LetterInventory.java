package ass6;

//Dibo Zhang
//CSE 143 BN
//Homework 1
//A class that stores and process a String of letters
//including sort in alphabetic order, addition, subtraction
//and number of letter edition methods
public class LetterInventory {

    //store the letter String that user initialized
    private String alphabetic = "";

    //ignore case of letters and non-alphabetic characters
    //store the input into global variable
    LetterInventory(String data) {
        String ignoreCase = data.toLowerCase();
        for (int i = 0; i < ignoreCase.length(); i++) {
            if (Character.isLetter(ignoreCase.charAt(i))) {
                alphabetic += ignoreCase.charAt(i);
            }
        }
    }

    //Pre:input letter should be valid alphabetic letter
    //(throws an IllegalArgumentException otherwise)
    //
    //Post:returns a count of how many of this letter are in the inventory
    public int get(char letter) {
        int count = 0;
        if (!Character.isLetter(letter)) {
            throw new IllegalArgumentException("input should be valid letter");
        }
        for (int i = 0; i < alphabetic.length(); i++) {
            if (alphabetic.charAt(i) == Character.toLowerCase(letter)) {
                count++;
            }
        }
        return count;

    }

    //Pre:input letter should be valid alphabetic letter
    //(throws an IllegalArgumentException otherwise)
    //input value should be non-negative (throws an IllegalArgumentException otherwise)
    //
    //Post:sets the count for the given letter to the given value
    public void set(char letter, int value) {
        if (value < 0) {
            throw new IllegalArgumentException("the input number should be non-negative");
        }
        if (!Character.isLetter(letter)) {
            throw new IllegalArgumentException("input should be valid letter");
        }
        char lowerLetter = Character.toLowerCase(letter);
        String withoutLetter = "";
        for (int i = 0; i < alphabetic.length(); i++) {
            if (alphabetic.charAt(i) != lowerLetter) {
                withoutLetter += alphabetic.charAt(i);
            }
        }
        alphabetic = withoutLetter;
        for (int i = 0; i < value; i++) {
            alphabetic += lowerLetter;
        }
    }

    //returns the sum of all of the counts in this inventory
    public int size() {
        return alphabetic.length();
    }

    //return true if the inventory is empty
    public boolean isEmpty() {
        return alphabetic.equals("");
    }

    //Returns a String representation of the inventory
    //with the letters all in lowerCase and in sorted order
    //and surrounded by square brackets
    public String toString() {
        String sorted = "";
        for (char character = 97; character < 123; character++) {
            for (int i = 0; i < alphabetic.length(); i++) {
                if (alphabetic.charAt(i) == character)
                    sorted += character;
            }
        }
        return "[" + sorted + "]";
    }

    //Takes a LetterInventory object
    //Constructs and returns a new LetterInventory object
    //that represents the sum of this letter inventory
    //and the other given LetterInventory
    public LetterInventory add(LetterInventory other) {
        String addition = alphabetic + other.toString();
        LetterInventory LIadd = new LetterInventory(addition);
        return LIadd;
    }

    //Takes a LetterInventory object
    //Constructs and returns a new LetterInventory object
    //that represents the result of subtracting
    //the other inventory from this inventory
    //return null if resulting count is negative
    public LetterInventory subtract(LetterInventory other) {
        String subtrResult = alphabetic;
        String subtr = other.toString().substring(1, other.toString().length() - 1);
        int indexNum;
        for (int i = 0; i < subtr.length(); i++) {
            indexNum = subtrResult.indexOf(subtr.charAt(i));
            if (indexNum < 0) {
                return null;
            } else {
                subtrResult = subtrResult.substring(0, indexNum)
                        + subtrResult.substring(indexNum + 1);
            }

        }
        LetterInventory LIsubtr = new LetterInventory(subtrResult);
        return LIsubtr;
    }

}