import java.util.*;
class Solution {
    final char[] arr = new char[]{'A','E','I','O','U'};
    Map<String, Integer> dict = new HashMap<>();
    int offset = 0;
    public int solution(String word) {
        dfs("");
        
        return dict.get(word);
    }
    
    void dfs(String data){
        if(!dict.containsKey(data)) dict.put(data, offset++);

        if(data.length() == 5){
            return;
        } 
        for(int i=0; i<arr.length; i++){
            dfs(data+arr[i]);
        }
    }
    
}