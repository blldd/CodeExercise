package ass5;
//Dibo Zhang
//CSE 143 BN
//Homework 5

import java.util.*;
import java.io.*;

public class GrammarSolver {

    //
    private SortedMap<String, List<String>> grammarmap;

    /*
    constructor
    */
    GrammarSolver(List<String> grammar) {
        if (grammar.size() == 0) {
            throw new IllegalArgumentException("valid grammar should be entered");
        }
//        assert grammar.size() != 0 : "Failed precondition: getAnagrams";

        this.grammarmap = new TreeMap<String, List<String>>();
        for (String line : grammar) {
            String[] parts = line.split("::=");
            if (this.grammarmap.containsKey(parts[0])) {
                throw new IllegalArgumentException("nonterminal should not be the same");
            }
            this.grammarmap.put(parts[0], new ArrayList<String>());
            String[] subparts = parts[1].split("[|]");
            for (String subp : subparts) {
                this.grammarmap.get(parts[0]).add(subp.trim());
            }
        }
    }

    /*
    check if grammar contains input symbol
    */
    public boolean grammarContains(String symbol) {
        return grammarmap.containsKey(symbol);
    }

    /*
    generate results given symbol and times
    */
    public String[] generate(String symbol, int times) {
        String[] output = new String[times];
        Random r = new Random();
        for (int i = 0; i < times; i++) {
            String result = "";
            result = generateNonterminal(symbol, r);
         /*
         
         */
            output[i] = result.substring(1);
        }
        return output;
    }

    /*
    return a string of symnbols given grammar
    */
    public String getSymbols() {
        return grammarmap.keySet().toString();
    }

    /*
    recursive generate nonterminal
     */
    private String generateNonterminal(String symbol, Random r) {
        String result = "";
        String store = grammarmap.get(symbol).get(r.nextInt(grammarmap.get(symbol).size()));
        String[] parts = store.split("[ \t]+");
        for (String s : parts) {
            if (grammarmap.containsKey(s)) {
                result += generateNonterminal(s, r);
            } else {
                result += " " + s;
            }
        }
        return result;
    }
}