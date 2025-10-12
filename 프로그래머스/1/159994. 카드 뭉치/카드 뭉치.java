import java.util.*;
class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {

        int nextCard = 0;
        int firstIdx = 0;
        int secondIdx = 0;
        
        while(nextCard < goal.length){
            
            String target = goal[nextCard];
            
            if(firstIdx < cards1.length && cards1[firstIdx].equals(target)){
                firstIdx++;
                nextCard++;
            }else if(secondIdx < cards2.length && cards2[secondIdx].equals(target)){
                secondIdx++;
                nextCard++;
            }else{
                return "No";
            }
        }
        
        
        return "Yes";
    }
}