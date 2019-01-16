public class Kata {
  public static String HighAndLow(String numbers) {
    
     String [] array = numbers.split(" ");
     int[] results = new int[array.length];
     int i = 0; 
       for ( String textValue : array ) {
        results[i] = Integer.parseInt(textValue.trim()); 
        i++; 
        } 
 
     int minValue = results[0]; 
     int maxValue = results[0]; 
      
        for(i=0; i<results.length; i++){ 
          if(results[i] <= minValue){ 
            minValue = results[i]; 
            }
          else if(results[i] >= maxValue){ 
            maxValue = results[i]; 
          } 
     }
  
    return String.valueOf(maxValue) + " " + String.valueOf(minValue);
  }
}
