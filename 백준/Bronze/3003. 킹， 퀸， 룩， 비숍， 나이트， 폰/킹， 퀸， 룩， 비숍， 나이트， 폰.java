import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
  
      Scanner scanner = new Scanner(System.in);
      
      int K = scanner.nextInt();
      int Q = scanner.nextInt();
      int L = scanner.nextInt();
      int V = scanner.nextInt();
      int N = scanner.nextInt();
      int P = scanner.nextInt();
      
      System.out.printf("%d %d %d %d %d %d",1-K,1-Q,2-L,2-V,2-N,8-P);
      

  
   
  }
}
