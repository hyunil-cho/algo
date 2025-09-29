class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        

        
        for(int i=0; i<signs.length; i++) {
        	
        	int temp = signs[i]?absolutes[i]:-1*absolutes[i];

        	answer+=temp;
        }
        
        
        return answer;
    }
}