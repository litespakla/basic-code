import javax.swing.JOptionPane;

  public class fibonacci_2 {

public static long fibonacci (int N){
long a=1;
long b=1;
int c=1;
long n;
if (N<1) {
System.out.println("The " + N + " Fibonacci doesn't exists");
}
else {
while(c<N){
n=a+b;
a=b;
b=n;
c++;
}}
return a;
}

public static void main(String[] args) {
  String num= JOptionPane.showInputDialog("What Fibonacci number you want to know?");
   int number= Integer.parseInt(num);
   long F=fibonacci(number);
   if (number>0){
 JOptionPane.showMessageDialog(null , "The " + number +"th Fibonacci number is  "  + F );
}}}
