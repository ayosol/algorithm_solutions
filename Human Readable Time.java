public class HumanReadableTime {
  public static String makeReadable(int number) {
    String hr, min, secs = "";

    if(number <= 0) return "00:00:00";
        
        if ((number%60) < 10) secs = "0" + (number%60);
        else secs = Integer.toString((number%60));

        if (((number / 60) % 60) < 10) min = "0" + ((number / 60) % 60);
        else min = Integer.toString(((number / 60) % 60));
      
        if ((number/3600) <= 9) hr = "0" + (number/3600);
        else hr = Integer.toString((number/3600));
    
    return hr + ":" + min + ":" + secs;
  }
}

****************************************************************************

public class HumanReadableTime {
  public static String makeReadable(int seconds) {
    return String.format("%02d:%02d:%02d", seconds / 3600, (seconds / 60) % 60, seconds % 60);
  }
}
