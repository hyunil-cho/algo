import java.util.*;
/**
1. 마킹 -> 2*2 형태가 존재하는지 확인. 존재할 경우, 마킹
2. 마킹된 데이터 삭제
3. 빈 자리로 데이터 이동(수직 낙하 이동)
4. 더 이상 마킹된 데이터가 없어질 때까지 1번 반복
**/
class Solution {
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        char[][] b = new char[m][n];
        
        for(int i=0; i<board.length; i++){
            String next = board[i];
            for(int j=0; j<next.length(); j++){
                b[i][j] = next.charAt(j);
            }
        }
        while(true){
            
            boolean[][] marking = new boolean[m][n];
            check(b, marking);
            int cnt = marking(b, marking);
            move(b);
            answer+=cnt;
            if(cnt == 0) break;
        }
                
        
        return answer;
    }
    
    void move(char[][] board){
        for(int i=board.length-1; i>=0; i--){
            for(int j=0; j<board[i].length; j++){
                if(board[i][j] == 'X'){
                    int sr = i;
                    while(sr >= 0 && board[sr][j] =='X'){
                        sr -= 1;
                    }
                    
                    if(sr>=0 && board[sr][j] !='X'){
                        board[i][j] = board[sr][j];
                        board[sr][j] = 'X';
                    }
                }
            }
        }
    }
    
    int marking(char[][] board, boolean[][] marking){
        int cnt = 0; 
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length; j++){
                if(marking[i][j]){
                    board[i][j] ='X';
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
    
    void print(char[][] board){
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length; j++){
                System.out.print(board[i][j]);
            }
            System.out.println("");
        }
    }
    
    void check(char[][] board, boolean[][] marking){
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length; j++){
                char target = board[i][j];
                if(target =='X') continue;
                if(i+1 < board.length && j+1 < board[i].length){
                    if(target ==board[i+1][j] && target == board[i][j+1] && target == board[i+1][j+1]){
                        
                        marking[i][j] = true;
                        marking[i+1][j] = true;
                        marking[i][j+1] = true;
                        marking[i+1][j+1] = true;
                        
                    }
                }
                
            }
        }
    
    }
}

