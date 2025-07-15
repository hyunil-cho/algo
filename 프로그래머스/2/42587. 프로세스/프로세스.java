import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((t1,t2)->Integer.compare(t2,t1));
        
        for(int next : priorities) pq.add(next);
        
        Queue<Item> que = new LinkedList<>();
        
        for(int i=0; i<priorities.length; i++){
            
            Item item = new Item(i, priorities[i]);
            que.add(item);    
            
        }
        int cnt = 0;
        while(!que.isEmpty()){
            Item next = que.poll();
            if(!pq.isEmpty() && pq.peek() == next.prior){
                pq.poll();
                cnt++;
                if(next.idx == location) return cnt;
            }else{
                que.add(next);
            }
            
        }
        
        
        
        return answer;
    }
}
class Item{
    int idx;
    int prior;
    Item(int idx, int prior){
        this.idx = idx;
        this.prior = prior;
    }
}