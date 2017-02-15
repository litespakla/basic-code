import javax.swing.JOptionPane;
public class pi_with_montecarlo {


  public static double randomNum (double L){   //Generate a random number
  double k= (Math.random()*L);
  return k;
  }

  public static double hits (double L, int N){
    double c=0;
    for (int i=0; i<N; i++){         //"p" is the position of the center of the match and "a" is the angle from the x axis
    double p=randomNum(2*L);
    double a=randomNum(Math.PI);  //Because symmetry, it's irrelevant if you divide by 2 or by 4
    double lenght=L*Math.sin(a)/2;

    if(2*L<=lenght+p || p-lenght<=0){  //If a match touch the y=0 or the y=2*L line, we account it
    c=c+1;
    }}
    return c;
  }

  public static double matches(){
  String numero1= JOptionPane.showInputDialog("How many matches?");  //How many matches do you want to throw?
    int N= Integer.parseInt(numero1);

  String numero2= JOptionPane.showInputDialog("Lenght of matches?");  //Lenght of the matches
    double L= Double.parseDouble(numero2);

    String numero3= JOptionPane.showInputDialog("How many trials?");  //How many matches do you want to throw?
      int T= Integer.parseInt(numero3);
  double R=0;
  for (int i=0; i<T; i++) {
    double k=hits(L, N);
      System.out.println("Result of trial " + (i+1)+ " is: " + N/k);
    R+=N/k;
  }
  return R/T;
  }

public static void main(String[] args) {
  double pi= matches();
  JOptionPane.showMessageDialog(null, "Pi is " + pi + " aproximately");
}}
