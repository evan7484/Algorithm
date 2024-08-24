import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
  
      Scanner scanner = new Scanner(System.in);
      
      int X = scanner.nextInt();
      int N = scanner.nextInt();
      
      for (int i = 0; i < N; i++){
        int pr = scanner.nextInt();
        int n = scanner.nextInt();
        
        X = X - (pr*n);
      }
      
      if (X == 0) {
        System.out.println("Yes");  
      }
      else{
        System.out.println("No");
      }
      
      

   
  }
}
