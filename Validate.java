public class Validate{
  public static boolean validate(String n){
    int result = 0; 
    int[] num = new int[n.length()];
    boolean alternate = false;
 
    for (int i = num.length - 1; i >= 0; i--) {
      
        num[i] = Integer.parseInt(n.substring(i, i + 1));
        //num[i] = n.charAt(i) - '0';
        if (alternate){
          num[i] *= 2;   
          
            if(num[i] > 9){
              num[i] = (num[i] % 10) + 1;
             }
          }
          result += num[i];
          alternate = !alternate;
      }
      return (result % 10 == 0);
//        if (result % 10 != 0) {return false;}
//      else {return true;}
  }
}