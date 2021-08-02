package practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class Method_Reference {
    public static void main(String[] args) {

        Consumer<String> func = text -> System.out.println(text);
        func.accept("Hello");
        // 실행 결과
        // Hello

        Consumer<String> func2 = System.out::println;
        func2.accept("Hello");
        // 실행 결과
        // Hello


        List<String> companies = Arrays.asList("google", "apple", "google", "apple", "samsung");
        List<String> test = new ArrayList<>();
        System.out.println(companies.getClass().getName());
        System.out.println(test.getClass().getName());

        // 1. lambda expression
        companies.stream().forEach(company -> System.out.println(company));
        // 2. static method reference
        companies.stream().forEach(System.out::println);
    }
}
