import javax.swing.JOptionPane;
public class pi_with_montecarlo {
  
  
  public static double randomNum (double L){   //Generate a random number
  double k= (Math.random()*2*L);
  return k;
  }
  
  public static double matches(){
  String numero1= JOptionPane.showInputDialog("How many matches?");  //How many matches do you want to throw?
    int N= Integer.parseInt(numero1);
    
  String numero2= JOptionPane.showInputDialog("Lenght of matches?");  //Lenght of the matches
    double L= Double.parseDouble(numero2);  
    
    double c=0;
    
    for (int i=0; i<N; i++){         //"p" is the position of the center of the match and "a" is the angle from the x axis
    double p=randomNum(L);
    double a=randomNum(Math.PI/4);  //Because symmetry, it's irrelevant if you divide by 2 or by 4
    double lenght=L*Math.sin(a)/2;
    
    if(2*L<=lenght+p || p-lenght<=0){  //If a match touch the y=0 or the y=2*L line, we account it
    c=c+1;
    }}
  return N/c;
  }  
  
public static void main(String[] args) {
  double pi= matches();
  System.out.println("PI: " + pi);
}}
