import java.util.*;
class Solution {
    String[][] relation;
    Map<String, List<String>> map = new HashMap<>();
    int numsOfRow;
    int keyNums;
    public int solution(String[][] relation) {
        this.relation = relation;
        int answer = 0;
        numsOfRow = relation.length;
        keyNums = relation[0].length;
        List<String> keys = new ArrayList<>();
        for(int cnt = 1; cnt <= keyNums; cnt++){
            dfs(cnt, 0, 0, new String[cnt], keys);
        }
        
        for(String[] rel : relation){
            
            for(String key : keys){
                
                String value = create(key, rel);
                map.putIfAbsent(key, new ArrayList<>());
                map.get(key).add(value);
            }
            
        }
                
        for(String key : keys){
            if(!map.containsKey(key)) continue;
            List<String> values = map.get(key);
            Set<String> extinct = new HashSet<>(values);
            if(values.size() == extinct.size()){
                System.out.println(values);
                answer++;
                removeKey(key);
            }            
        }
        
                
        return answer;
    }
    
    void removeKey(String key){
        
        Iterator<String> keys = map.keySet().iterator();
        while(keys.hasNext()){
            String n = keys.next();
            int hitCnt = 0;
            for(int i=0; i<key.length(); i++){
                if(n.indexOf(key.charAt(i))>=0) hitCnt++;
            }
            
            
            if(hitCnt == key.length()) keys.remove();
        }
    }
    
    String create(String key, String[] rel){
        StringBuilder b= new StringBuilder();
        for(int i=0; i<key.length(); i++){
            b.append(rel[key.charAt(i)-'0']);
        }
        return b.toString();
    }
    
    void dfs(int cnt, int curCnt, int curIdx, String[] result, List<String> keys){
        if(cnt == curCnt){
            StringBuilder b = new StringBuilder();
            for(String r : result){
                b.append(r);
            }
            keys.add(b.toString());
            
        }else{
            
            for(int i=curIdx; i<keyNums; i++){
                result[curCnt] = i+"";
                dfs(cnt, curCnt+1, i+1, result, keys);
            }
            
        }
    }
}