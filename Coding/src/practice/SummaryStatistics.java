package practice;

import java.util.Arrays;
import java.util.IntSummaryStatistics;
import java.util.List;

public class SummaryStatistics {
    public static void main(String[] args) {
        List<String> langs =
                Arrays.asList("java", "kotlin", "haskell", "ruby", "javascript");
        IntSummaryStatistics stats = langs.stream()
                .mapToInt((lang) -> (lang.length()))
                .summaryStatistics();

        List<String> companies =
                Arrays.asList("google", "apple", "google", "apple", "samsung");
        IntSummaryStatistics stats2 = companies.stream()
                .mapToInt((lang) -> (lang.length()))
                .summaryStatistics();

        stats.combine(stats2);

        System.out.println("Max: " + stats.getMax());
        System.out.println("Min: " + stats.getMin());
        System.out.println("Average: " + stats.getAverage());
        System.out.println("Count: " + stats.getCount());
    }
}
