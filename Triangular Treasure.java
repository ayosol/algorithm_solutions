public class Triangular {
    public static int triangular(int n) {
    
      if (n <= 0) return 0;
      
      for (int i = 1; i <= n; i++){
//         n = n + (n - 1);
        n = (1 + n) * n / 2;
        return n;
      }
      
      return n;

    }
}
