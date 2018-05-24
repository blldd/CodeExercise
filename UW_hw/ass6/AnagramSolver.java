package ass6;

import java.util.*;

//Dibo Zhang
//CSE 143 BN
//Homework 6
// 

public class AnagramSolver {

    private Map<String, LetterInventory> dictionary;                //dictionary map
    private Map<String, LetterInventory> anaMap;                    //construct a small map to find more efficient

    public AnagramSolver(List<String> list) {                       //constructor
        dictionary = new HashMap<String, LetterInventory>();        //construct dictionary
        for (int i = 0; i < list.size(); i++) {
            String keyStr = list.get(i);
            LetterInventory valLi = new LetterInventory(keyStr);
//            valLi = new LetterInventory(valLi.toString().substring(1, valLi.toString().length() - 1));
            dictionary.put(keyStr, valLi);                          //key : key string    value : LetterInventory
        }

//        for (String keyStr : dictionary.keySet()) {
//            LetterInventory val = dictionary.get(keyStr);
//            System.out.println(keyStr + " -- " + val.toString());
//            System.out.println(keyStr.hashCode());
//            System.out.println(val.hashCode());
//            System.out.println(keyStr.hashCode() ^ val.hashCode());
//            System.out.println(hashCode());
//        }
//        System.out.println("-------------------------------");
//
//        Iterator iter = dictionary.entrySet().iterator();
//        while (iter.hasNext()) {
//            Map.Entry entry = (Map.Entry) iter.next();
//            String key = (String) entry.getKey();
//            LetterInventory integ = (LetterInventory)entry.getValue();
//            System.out.println(key + " -- " + integ.toString());
//        }
    }

    public void print(String phrase, int max) {
        if (max < 0 || phrase == null) {
            throw new IllegalArgumentException();
        }

        LetterInventory input = new LetterInventory(phrase);        //user input
        input = new LetterInventory(input.toString().substring(1, input.toString().length() - 1));
//        System.out.println(input.toString());
//        System.out.println(inputSort.toString());
        anaMap = new HashMap<String, LetterInventory>();            //store anagram by map
        List<List<String>> result = new ArrayList<List<String>>();

        for (String keyStr : dictionary.keySet()) {                 //traverse dictionary
            if (input.subtract(dictionary.get(keyStr)) != null)     //store key value with anagram map if find subString of input
                anaMap.put(keyStr, dictionary.get(keyStr));
        }
//        for (int i = 0; i < dictionary.keySet().size(); i++) {                                     //???
//            if (input.subtract(dictionary.get(dictionary.keySet().iterator().next())) != null) {   //???
//                anaMap.add(dictionary.get(dictionary.keySet().iterator().next()));                 //???
//            }
//        }
        ArrayList<String> anaList = new ArrayList<String>();
        printResult(input, anaList, max, anaMap, 0);          //recursive method
    }

    private void printResult(LetterInventory input,
                             ArrayList<String> anaList, int max,
                             Map<String, LetterInventory> anaDict, int size) {

        LetterInventory iterLi;                                     //iterator key in anagram map
        LetterInventory leftLi;                                     //left LetterInventory after subtract
        if (size < max || max == 0) {
            Iterator<String> it = anaDict.keySet().iterator();
            if (!it.hasNext() && size == 0) {                       //output [] if 1234
                System.out.println(anaList.toString());
            }
            while (it.hasNext()) {
                String key = it.next();
                iterLi = new LetterInventory(key);
                leftLi = input;
                if (leftLi.subtract(iterLi) != null) {
                    anaList.add(key);                               //add key into anagram list if input contains iterator key
                    leftLi = input.subtract(iterLi);
                    if (leftLi.isEmpty()) {
                        System.out.println(anaList.toString());     //print if match
                    } else {
                        printResult(leftLi, anaList, max, anaDict, size + 1);   //recursive if there is sth left
                    }
                    anaList.remove(anaList.size() - 1);       //backtracking
                }
            }
        }
    }
}


//
//
//public class AnagramSolver {
//    //
//    private HashMap<String, List<String>> dictionary;
//
//    /*
//
//    */
//    AnagramSolver(List<String> list) {
//        dictionary = new HashMap<String, List<String>>();
//
//        for (int i = 0; i < list.size(); i++) {
//            LetterInventory li = new LetterInventory(list.get(i));
//            String keyStr = li.toString().substring(1, li.toString().length() - 1);
//            List<String> valList = dictionary.get(keyStr);
//            valList.add(list.get(i));
//            dictionary.put(keyStr, valList);    //???
//        }
//    }
//
//    /*
//    Pre: max should not be less than 0 (throw an IllegalArgumentException otherwise)
//    */
//    public void print(String phrase, int max) {
//        if (max < 0) {
//            throw new IllegalArgumentException();
//        }
//        LetterInventory input = new LetterInventory(phrase);
//        List<String> result = new ArrayList<String>();
//        List<LetterInventory> subdictionary = new ArrayList<LetterInventory>();
//        for (int i = 0; i < dictionary.keySet().size(); i++) {                                     //???
//            if (input.subtract(dictionary.get(dictionary.keySet().iterator().next())) != null) {   //???
//                subdictionary.add(dictionary.get(dictionary.keySet().iterator().next()));          //???
//            }
//        }
//        if (max == 0) {
//            max--;
//        }
//        printResult(subdictionary, result, input, max);
//    }
//
//    /*
//
//
//    private void printResult(List<LetterInventory> subdictionary, List<String> result, LetterInventory input, int max, int ind) {
//        if (input.isEmpty()) {
//            System.out.println(result);
//        } else if (max != 0) {
//            for (int i = 0; i < subdictionary.size(); i++) {
//                if (input.subtract(subdictionary.get(i)) != null) {
//                    LetterInventory subletters = input.subtract(subdictionary.get(i));
////                    result.add(dictionary.keySet().iterator().next());
////                    printResult(subdictionary, subletters, input, max - 1);
//                    result.remove(result.size() - 1);
//                }
//            }
//        }
//    }
//*/
//}