import java.util.*;
class Solution {
    public String solution(String s, int n) {
       StringBuilder b = new StringBuilder();
        for(char c : s.toCharArray()){
            b.append(push(c,n));
        }
        return b.toString();
    }
    
    char push(char c, int n){
        if(!Character.isAlphabetic(c)) return c;
        
        int offset = Character.isUpperCase(c) ? 'A':'a';
        int pos = c - offset;
        pos = (pos + n) % 26;
        return (char) (offset+pos);
    }
}