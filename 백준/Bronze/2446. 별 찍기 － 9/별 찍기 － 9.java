import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = 0;
        N = scanner.nextInt();

        for(int i = 1; i < N+1; i++){
            for (int a = 0; a < i-1; a++){
                System.out.print(" ");
            }
            for (int b = 0; b < (2*N-1)-(i-1)*2; b++) {
                System.out.print("*");
            }
            System.out.println("");
        }
        for(int i = 1; i < N; i++){
            for (int a = 0; a < N-1-i; a++){
                System.out.print(" ");
            }
            for (int b = 0; b < 3+(i-1)*2; b++) {
                System.out.print("*");
            }
            System.out.println("");
        }


    }
}