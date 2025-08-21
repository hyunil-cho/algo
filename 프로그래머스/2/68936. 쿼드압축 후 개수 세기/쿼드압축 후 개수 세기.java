class Solution {
    
    int one = 0;
    int zero = 0;
    
    public int[] solution(int[][] arr) {
        int[] answer = {};
        compress(arr, 0, 0, arr.length);
        return new int[]{zero, one};
    }
    
    void compress(int[][] arr, int startRow,int startCol, int len){
        
        int target = -1;
        boolean isFail = false;
        for(int i=startRow; i<startRow+len && !isFail; i++){
            for(int j=startCol; j<startCol+len && !isFail; j++){
                if(target == -1) target = arr[i][j];
                else{
                    if(target != arr[i][j]) {
                        isFail = true;
                        break;
                    };
                }
            }
        }
        
        if(!isFail){
            
            if(target == 1) one+=1;
            if(target == 0) zero+=1;
            
        }else{
            //사등분 로직
            //1사분면
            len = len / 2;
            compress(arr, startRow, startCol+len, len);
            //2사분면
            compress(arr, startRow, startCol, len);
            //3사분면
            compress(arr, startRow+len, startCol, len);
            //4사분면
            compress(arr, startRow+len, startCol+len, len);
        }        
    }
}