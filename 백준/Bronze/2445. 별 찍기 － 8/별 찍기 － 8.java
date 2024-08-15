import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = 0;
        N = scanner.nextInt();

        for(int i = 1; i < N+1; i++){
            for (int a = 0; a < i; a++){
                System.out.print("*");
            }
            for (int b = 0; b < 2*N-2*i; b++){
                System.out.print(" ");
            }
            for (int c = 0; c < i; c++){
                System.out.print("*");
            }
            System.out.println("");
        }
        for(int i = 1; i < N; i++){
            for (int a = 0; a < N-i; a++){
                System.out.print("*");
            }
            for (int b = 0; b < 2*i; b++){
                System.out.print(" ");
            }
            for (int c = 0; c < N-i; c++){
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}