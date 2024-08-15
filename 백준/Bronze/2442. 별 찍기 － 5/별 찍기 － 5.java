import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        for (int i = 1; i < N+1; i++){

            for (int s = 0; s < N - i;s++){
                System.out.print(" ");
            }
            for(int j = 1; j <2*i; j++){
                System.out.print("*");
            }

            System.out.println();
        }
}
}
