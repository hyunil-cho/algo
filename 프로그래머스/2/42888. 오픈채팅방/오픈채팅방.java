/**
1. 사용자의 채팅창 IN/OUT 이력을 ID로 추적한다.
2. 사용자의 닉네임 변경 이력을 ID로 추적하며, 마지막으로 사용된 닉네임을 추적한다.
3. 1번을 사용자의 닉네임으로 변경하여 노출한다.

**/
import java.util.*;
class Solution {
    List<String> his = new ArrayList<>();
    Map<String,String> mapping = new HashMap<>();
    
    public String[] solution(String[] records) {
        String[] answer = {};
        
        for(String record : records){
            
            String[] history = record.split(" ");
            String type = history[0];
            
            if(type.equals("Enter")){
                his.add(String.format("%s님이 들어왔습니다.",  history[1]));
                mapping.put(history[1], history[2]);
            }
            
            if(type.equals("Leave")){
                his.add(String.format("%s님이 나갔습니다.",  history[1]));
            }
            
            if(type.equals("Change")){
                mapping.put(history[1], history[2]);
            }
            
        }

        for(int i=0; i<his.size(); i++){
            String raw = his.get(i);
            String dd =raw.substring(0, raw.indexOf("님"));
            String id = mapping.get(dd);
            raw = raw.replace(dd, id);
            his.set(i, raw);
            
        }
                    
        
        return his.stream().toArray(String[]::new);
    }
}