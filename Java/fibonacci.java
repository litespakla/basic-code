import javax.swing.JOptionPane;

  public class fibonacci {
    
  public static int fibonacci (int N){
    int F=0;
     if (N==1){
       F=0;
    }
     if (N==2){
       F=1;
    }
     if (N>2) {
       F=fibonacci(N-1)+fibonacci(N-2);
    }
  return F;  
  } 
    
   public static void main(String[] args) {
     String num= JOptionPane.showInputDialog("What Fibonacci number you want to know?");
      int number= Integer.parseInt(num);
      int F=fibonacci(number);
    JOptionPane.showMessageDialog(null , "The " + number +" Fibonacci number is  "  + F );
   }}
