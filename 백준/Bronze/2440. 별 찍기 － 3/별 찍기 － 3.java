import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        for (int i = N; i > 0; i--){
            for(int j = 0; j < N; j++){
                System.out.printf("*");
            }
            System.out.println();
            N -= 1;
        }
}
}