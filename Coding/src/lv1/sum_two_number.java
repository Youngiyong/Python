//package lv1;
//
//
//import java.util.Collections;
//import java.util.ArrayList;
//import java.util.HashSet;
//import java.util.List;
//import java.util.Set;
//
//
//public class sum_two_number {
//    public static void main(String[] args) {
//        Solution s = new Solution();
//        int[] numbers = { 2, 1, 3, 4, 1};
//        s.solution(numbers);
//    }
//}
//
//class Solution {
//    public List<Integer> solution(int[] numbers) {
//        Set<Integer> answer = new HashSet<>();
//        int idx=0;
//        for(int i=0; i<numbers.length; i++){
//            for(int j=0+idx; j<numbers.length; j++){
//                if(j+1==numbers.length) {
//                    break;
//                }
//                answer.add(numbers[i] + numbers[j+1]);
//            }
//            idx++;
//        }
//        List<Integer> result = new ArrayList<>(answer);
//        Collections.sort(result);
//
//        return result;
//    }
//}