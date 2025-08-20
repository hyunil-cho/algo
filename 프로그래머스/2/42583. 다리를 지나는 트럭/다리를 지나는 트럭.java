import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] ts) {
        int answer = 0;
        Deque<Truck> trucks = new LinkedList<>();
        int cw = 0;
        int second = 0;
        int idx = 0;
        while(idx < ts.length){
            
            while(!trucks.isEmpty() && (second - (trucks.peek().time)) >= bridge_length){
                cw -=trucks.pollFirst().weight;
            }
            
            Truck nt = new Truck(second,ts[idx]);
            if(cw + nt.weight <= weight){
                cw += nt.weight;
                idx += 1;
                trucks.addLast(nt);
            }
            
            
            second+=1;
            
        }
        
        if(trucks.isEmpty()){
            return second;
        }
        
        return ((trucks.pollLast().time+1)+bridge_length);
    }
}

class Truck{
    int weight;
    int time;
    Truck(int time, int weight){
        this.time = time;
        this.weight = weight;
    }
}