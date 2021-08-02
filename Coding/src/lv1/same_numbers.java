//package lv1;
//import java.util.*;
//
//public class same_numbers {
//    public static void main(String[] args) {
//        Solution s = new Solution();
//        int[] numbers = {1,1,3,3,4,4,5,6,5};
//        s.solution(numbers);
//    }
//}
//
//class Solution {
//    public int[] solution(int []arr) {
//        List<Integer> answer = new ArrayList<>();
//        int temp = -1;
//        for (Integer num : arr){
//            if(temp != num){
//                answer.add(num);
//                temp = num;
//            }
//        }
//
//
//        return answer.stream().mapToInt(Integer::intValue).toArray();
//    }
//}
//
//
