//package lv2;
//
//public class state_124 {
//    public static void main(String[] args) {
//
//        Solution s = new Solution();
//        System.out.println(s.solution(100));
//    }
//}
//
//class Solution {
//    public String solution(int n) {
//        String answer = "";
//
//        while (n>0) {
//            int num = n % 3;
//            answer = (num==0 ? "4" : (num==1 ? "1" : "2")) + answer;
//            n = (n-1)/3;
//        }
//
//        return answer;
//    }
//}