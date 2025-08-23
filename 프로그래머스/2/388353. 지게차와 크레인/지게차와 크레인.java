/**
1. 컨테이너를 꺼낼 때, 상하좌우 중 최소 한 개의 면이 열려있거나, 벽에 붙은 경우, 뽑을 수 있다.

**/
import java.util.*;
class Solution {
    
    int[] nr = new int[]{-1,1,0,0};
    int[] nc = new int[]{0,0,-1,1};
    
    public int solution(String[] storage, String[] requests) {
        int answer = 0;

        char[][] board = new char[storage.length][storage[0].length()];
        for(int i=0; i<storage.length; i++){
            for(int j=0; j<storage[0].length(); j++){
                board[i][j] = storage[i].charAt(j);
            }
        }   
        
        List<Integer[]> targets = new ArrayList<>();
        
        for(String req : requests){
            boolean isC = req.length() == 2;
            char r = req.charAt(0);
            for(int i=0; i<board.length; i++){
                for(int j=0; j<board[i].length; j++){
                    char val = board[i][j];
                    if(r != val) continue;
               
                    boolean isOkay = isC ? true : check(i,j, board.length, board[0].length, board);
                                
                    if(isOkay){
                        targets.add(new Integer[]{i,j});
                    }              
                }
            }        
            
            for(Integer[] next : targets){
                board[next[0]][next[1]] = '#';
            }
            
        }
        
        for(int i=0; i<board.length; i++){
          for(int j=0; j<board[i].length; j++){
              System.out.print(board[i][j]);
            if(board[i][j] != '#') {
              answer++;
            }
          }
            System.out.println("");
        }
                  
        
        return answer;
    }
    
       public boolean check(int x, int y, int n, int m, char[][] storage){
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        visited[x][y] = true;
        queue.add(new int[]{x,y});

        while(!queue.isEmpty()){
            int[] tmp = queue.poll();
            int nx = tmp[0];
            int ny = tmp[1];

            for(int i = 0 ; i < 4; i++){
                int nextX = nx + nr[i];
                int nextY = ny + nc[i];

                if(nextX < 0 || nextX > n-1 || nextY < 0 || nextY > m-1) return true;

                if(!visited[nextX][nextY] && storage[nextX][nextY] == '#'){
                    visited[nextX][nextY] = true;
                    queue.add(new int[]{nextX, nextY});
                }
            }
        }
        return false;
    }
}