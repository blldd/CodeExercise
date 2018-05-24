package ass4b;

//Dibo Zhang
//CSE 143 BN
//Homework 4 Bonus
//improve on two flaws in the original HangmanManager:
//modify the record method so that it wins immediately if it can when the user is down to one guess
// (making the program even more evil)
//modify the words() and guesses() methods so that they prevent a client from changing our internal data structures


import java.util.*;

public class HangmanManager2 extends HangmanManager {
    public HangmanManager2(Collection<String> dictionary, int length, int max) {
        super(dictionary, length, max);
    }

    private void fillInMap1(Map<String, Set<String>> words, Set<String> patternCollect, char guess) {
        Iterator<String> itr = words().iterator();

        while (itr.hasNext()) {
            String currentPattern = "";
            String word = itr.next();
            int flag = 0;
            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) == guess) {
                    flag = 1;
                    currentPattern = currentPattern + guess;
                } else {
                    currentPattern = currentPattern + super.getPattern().charAt(i);
                }
            }
            if (flag == 0) {
                patternCollect.add(currentPattern);
                if (!words.containsKey(currentPattern)) {
                    words.put(currentPattern, new TreeSet<String>());
                }
                words.get(currentPattern).add(word);
            }

        }
    }

    private void findPattern1(Map<String, Set<String>> words, Set<String> patternCollect) {
        int count = 0;
        Iterator<String> itr = patternCollect.iterator();
//
//        System.out.println("----------------------pre------------------------");
//        for (String s:words.keySet()){
//            System.out.println(s);
//            for (String s2:words.get(s)) {
//                System.out.println("-->" + s2);
//            }
//        }
//        System.out.println("----------------------aft------------------------");

        while (itr.hasNext()) {
            String patternItr = itr.next();
            int sizeOfSet = words.get(patternItr).size();
            if (sizeOfSet > count) {
                count = sizeOfSet;
                super.setPattern(patternItr);
            }
        }
        super.setWordsList(words.get(super.getPattern()));
    }

    @Override
    public int guessesLeft() {
        return super.guessesLeft();
    }

    /*
     In particular, your class should create new unmodifiable versions of each set
     if and only if there is a new object being returned for the original set.
     For example, suppose that on 10 calls to the words() method, there are four different actual set objects returned.
     Then your class should create four different unmodifiable sets.
     If you create fewer than four, then your class won’t work.
     If you create more than four, then you won’t receive the credit.
     */
    @Override
    public Set<String> words() {
        Set<String> set1 = super.words();

//        Set<String> set2 = Collections.unmodifiableSet(set1);
        return set1;
    }

    @Override
    public Set<Character> guesses() {
        Set<Character> set1 = super.guesses();

//        Set<Character> set2 = Collections.unmodifiableSet(set1);
        return set1;
    }

    /*
    We will accomplish this by overriding the record method.
    It will still call the superclass version of the method to do most of the work.
    But before doing so, it will check to see if the user has just one guess left.

    If so, then it will go through the current set of words
    and pick the first word that does not contain the letter being guessed.

    If such a word can be found, then it calls the clear method on the current list of words
    and then adds this word back into the current set of words.
    That way when the superclass version of record is called, it will find just one word to work with.
    That one word will cause the user to lose the game immediately.

    If the number of guesses left is not 1 or if no such word can be found,
    then it simply calls the superclass version of the record method so that the behavior is unchanged.
     */
    @Override
    public int record(char guess) {
        if (guessesLeft() == 1) {
            Map<String, Set<String>> words = new TreeMap<String, Set<String>>();
            Set<String> patternCollect = new TreeSet<String>();
            super.guesses().add(guess);
            fillInMap1(words, patternCollect, guess);
            findPattern1(words, patternCollect);

//            Set<String> set1 = super.words();
//            Set<String> set2 = Collections.unmodifiableSet(set1);
//
            Set<String> w = super.words();
            System.out.println(w.size());
            if (w.size() > 0) {
                Iterator<String> itr = w.iterator();

//            for (String s:words.keySet()){
//                System.out.println(s);
//                for (String s2:words.get(s)) {
//                    System.out.println("-->" + s2);
//                }
//            }

                if (itr.hasNext()) {
                    String target = itr.next();
                    super.setWordsList(null);
                    Set<String> targetSet = new TreeSet<String>();
                    targetSet.add(target);
                    super.setWordsList(targetSet);
                    int countOfGuess = 0;
                    int guessNum = super.guessesLeft();
                    super.setGuessNumber(guessNum - 1);
                    return countOfGuess;
                } else {
                    return super.record(guess);
                }
            } else{
                return super.record(guess);
            }

        } else {
            return super.record(guess);
        }

    }
}
