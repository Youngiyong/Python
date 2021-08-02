//package lv2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;


//public class phone_book {
//    public static void main(String[] args) {
//        Solution s = new Solution();
//        String[] phone_book = {"123", "456", "1234", "1234"};
//        System.out.println(s.solution(phone_book));
//    }
//}

//class Solution {
//    public boolean solution(String[] phone_book) {
//        boolean answer = true;
//        HashMap<String, String> hm = new HashMap<>();
//
//        for( String input : phone_book ) {
//            hm.put(input, input);
//        }
//
//        for ( String target : phone_book) {
//            for( int i=0; i< target.length(); i++) {
//                if( hm.containsKey(target.substring(0,i)) ) {
//                    return false;
//                }
//                else if ( hm.get(target.substring(0,i)) != null) {
//                    return false;
//                }
//            }
//
//        }
//        return answer;
//    }
//}
//class Solution {
//    public boolean solution(String[] phone_book) {
//        Arrays.sort(phone_book);
//        List<String> listCollection = Arrays.asList(phone_book);
//        long cnt = 0;
//        boolean answer = true;
//        for(String s: phone_book){
//            cnt = listCollection.stream().filter((a) -> a.startsWith(s)).count();
//            if(cnt>1){
//                answer = false;
//                break;
//            }
//        }
//
//        return answer;
//    }
//}
