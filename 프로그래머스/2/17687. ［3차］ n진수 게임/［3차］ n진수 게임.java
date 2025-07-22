/**
    

**/
import java.util.*;
class Solution {
    Map<Integer,String> table= Map.of(10,"A",11,"B",12,"C",13,"D",14,"E",15,"F");
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        int cnt = 0;
        int nextCnt = 0;
        int curIdx = 0;
        while(cnt < t){
            
            String bin = convert(n, nextCnt);
            nextCnt++;
            for(int i=0; i<bin.length() && cnt < t; i++){
                
                char next = bin.charAt(i);
                if(curIdx == p-1){
                    answer+=next;
                    cnt++;
                }
                curIdx++;
                if(curIdx == m) curIdx = 0;
                 
            }
            
            
        }
        
        
        return answer;
    }
    
    String convert(int n, int target){
        if(n == 2) return Integer.toBinaryString(target);
        StringBuilder b = new StringBuilder();
        while(target >= n){
            int remain = target % n;
            if(!table.containsKey(remain)) b.append(remain);
            else b.append(table.get(remain));
            target = target / n;
        }
        if(table.containsKey(target)) b.append(table.get(target));
        else b.append(target);
                                               
        b.reverse();
        return b.toString();
        
        
    }
    
}