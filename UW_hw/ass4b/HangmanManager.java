package ass4b;
//Dibo Zhang
//CSE 143 BN
//Homework 4
//It stores a wordslist and a pattern.
//It can select the pattern with most words according to users guesses
//and store into the wordslist.

import java.util.*;

public class HangmanManager {

    //store the current wordslist
    private Set<String> wordsList;

    //store the letter that has already been guessed
    private Set<Character> guessLetter;

    //store the number of guess the user has left
    private int guessNumber;

    //store the pattern with most words
    private String pattern;


    /*
        Pre:length should not be less than 1, max should be larger than 0
        throw IllegalArgumentException otherwise
        store Collection<String> dictionary, int max into
        global varible Set wordsList and int guessNumber
        initialize Set guessLetter, String pattern
        */
    public HangmanManager(Collection<String> dictionary, int length, int max) {
        if (length < 1 || max < 0) {
            throw new IllegalArgumentException("invalid entrance of wordlength or maximum guess");
        }
        guessNumber = max;
        wordsList = new TreeSet<String>();
        guessLetter = new TreeSet<Character>();
        pattern = "";
        for (int i = 0; i < length; i++) {
            pattern = pattern + "-";
        }
        Iterator<String> itr = dictionary.iterator();
        while (itr.hasNext()) {
            String word = itr.next();

            if (word.length() == length) {
                wordsList.add(word.toLowerCase());
            }
        }
    }

    /*
    return the Set current list of words
    */
    public Set<String> words() {
        return wordsList;
    }

    public void setWordsList(Set<String> wordsList) {
        this.wordsList = wordsList;
    }

    /*
        return the number of guess left
        */
    public int guessesLeft() {

        return guessNumber;
    }

    public void setGuessNumber(int guessNumber) {
        this.guessNumber = guessNumber;
    }

    /*
    return the Set of already guessed letters
    */
    public Set<Character> guesses() {
        return guessLetter;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public String getPattern() {
        return pattern;
    }

    /*
    Pre: the wordsList should not be empty
    throw IllegalStateException otherwise
    Post:return String pattern with one blank apart of each letters
    */
    public String pattern() {
        if (wordsList.isEmpty()) {
            throw new IllegalStateException();
        }
        String patternBlank = "" + pattern.charAt(0);
        for (int i = 1; i < pattern.length(); i++) {
            patternBlank = patternBlank + " " + pattern.charAt(i);
        }
        return patternBlank;
    }

    /*
    Pre:guessnumber should be larger than 1 and wordsList should not be empty
    throw IllegalStateException otherwise
    Set guessLetter should not contains the character guess
    throw IllegalArgumentException otherwise
    change the pattern and wordsList according to the guess
    Post:return number of occurrences of the guessed letter
    */
    public int record(char guess) {
        if (guessNumber < 1 || wordsList.isEmpty()) {
            throw new IllegalStateException();
        }
        if (guessLetter.contains(guess)) {
            throw new IllegalArgumentException();
        }
        Map<String, Set<String>> words = new TreeMap<String, Set<String>>();
        Set<String> patternCollect = new TreeSet<String>();
        guessLetter.add(guess);
        fillInMap(words, patternCollect, guess);
        findPattern(words, patternCollect);
        int countOfGuess = 0;
        for (int i = 0; i < pattern.length(); i++) {
            if (pattern.charAt(i) == guess) {
                countOfGuess++;
            }
        }
        if (countOfGuess == 0) {
            guessNumber--;
        }
        return countOfGuess;
    }

    /*
    private method
    take Map words, Set patternCollect, char guess as parameters
    create different patterns and fill the words into the Map with these patterns as key
    */
    protected void fillInMap(Map<String, Set<String>> words, Set<String> patternCollect, char guess) {
        Iterator<String> itr2 = wordsList.iterator();
        while (itr2.hasNext()) {
            String currentPattern = "";
            String word = itr2.next();
            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) == guess) {
                    currentPattern = currentPattern + guess;
                } else {
                    currentPattern = currentPattern + pattern.charAt(i);
                }
            }
            patternCollect.add(currentPattern);
            if (!words.containsKey(currentPattern)) {
                words.put(currentPattern, new TreeSet<String>());
            }
            words.get(currentPattern).add(word);
        }
    }

    /*
    private method
    take Map words, Set patternCollect as parameters
    Find the pattern with most words and store the pattern
    and change the wordsList to the Set of words of the pattern
    */
    protected void findPattern(Map<String, Set<String>> words, Set<String> patternCollect) {
        int count = 0;
        Iterator<String> itr3 = patternCollect.iterator();
        while (itr3.hasNext()) {
            String patternItr = itr3.next();
            int sizeOfSet = words.get(patternItr).size();
            if (sizeOfSet > count) {
                count = sizeOfSet;
                pattern = patternItr;
            }
        }
        wordsList = words.get(pattern);
    }

}