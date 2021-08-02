package lv1;

import java.util.Arrays;
import java.util.Comparator;

public class string_sort {
    public static void main(String[] args) {

    }
}

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};

        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if(o1.charAt(n) > o2.charAt(n))
                    return 1;
                else if(o1.charAt(n) == o2.charAt(n))
                    return o1.compareTo(o2);
                else
                    return -1;
            }
        });
        return answer;
    }
}
