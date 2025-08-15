import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        Object[] arrs= Arrays.stream(numbers)
            .boxed()
            .map(String::valueOf)
            .sorted((a,b)->{
                String aFirst = a+b;
                String bFirst = b+a;
                return Integer.compare(Integer.valueOf(bFirst), Integer.valueOf(aFirst));
            }).toArray();
        
        for(Object next : arrs){
            answer+=next.toString();
        }
        
        while(answer.startsWith("0") && answer.length()>1){
            answer = answer.substring(1);
        }
        
        return answer;
    }
}