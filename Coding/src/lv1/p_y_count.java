//package lv1;
//
//import java.util.Arrays;
//import java.util.Locale;
//
//
//public class p_y_count {
//
//    public static void main(String[] args) {
//
//        Solution s = new Solution();
//        System.out.println(s.solution("Pyyp"));
//    }
//}
//
//
//class Solution {
//    boolean solution(String s) {
//        boolean answer = true;
//
//        s = s.toUpperCase();
//        long cnt_y = Arrays.asList(s.split("")).stream().filter(x -> x.contains("Y")).count();
//        long cnt_p = Arrays.asList(s.split("")).stream().filter(x -> x.contains("P")).count();
//
//        return cnt_p == cnt_y ? answer : false;
//    }
//}