//package lv1;
//
//import java.util.HashMap;
//
//public class finish_course {
//    public static void main(String[] args) {
//        Solution s = new Solution();
//        String[] participant = new String[]{"mislav", "stanko", "mislav", "ana"};
//        String[] completion = new String[]{"stanko", "ana", "mislav"};
//        System.out.println(s.solution(participant, completion));
//    }
//}
//
//class Solution {
//    public String solution(String[] participant, String[] completion) {
//
//        HashMap<String, Integer> map = new HashMap<>();
//        String result = "";
//        for (String s : participant) map.put(s, map.getOrDefault(s, 0) + 1);
//        for (String s : completion) map.put(s, map.getOrDefault(s, 0) -1);
//        for (String s : map.keySet()) if(map.get(s)==1) result = s;
//
//        return result;
//    }
//}