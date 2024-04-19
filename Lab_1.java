import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n, i, s;
        s = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter value for N");
        n = scanner.nextInt();
        scanner.close();
        for (i = 1; i < n; i++) {
            if (i % 2 == 0) {
                s = s + i;
                System.out.println("Current value i=" + i + " S=" + s);
            }
        }
        System.out.println("Final result sum is S=" + s);
    }
}


