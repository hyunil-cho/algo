class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        
        for(int i=0; i<arr1.length; i++){
            int[] next1 = arr1[i];
           
            for(int j=0; j<arr2[0].length; j++){
                int result = 0;
                for(int z =0; z<next1.length; z++){
                    result+= next1[z] * arr2[z][j];
                }
                answer[i][j] = result;
                
            }
            
        }
        
        return answer;
    }
}