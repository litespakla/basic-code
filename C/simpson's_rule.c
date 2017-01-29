#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int integral (double a, double b, int N);

int static parameters (){
double a;
double b;  //Integration interval (a,b)
int N;
  printf("\nIntegration interval?: ");
  scanf("%lf %lf", &a, &b);

  printf("\nHow many subintervals?: ");  // N subintervals
  scanf("%i", &N);
    printf("\nIntegration interval: [%g,%g]", a, b);
integral(a, b, N);
return 0;
}

double funcion (double x) //function
{
    double f=(exp(-0.3*x)*cos(4+x))/(log(x)); //Write function here
    return (f);
}

int integral (double a, double b, int N) //Integral with Simpson's rule
{
   /*double h=b-a;
   double I=(h/3)*(funcion(a)+4*funcion(a+h/2)+funcion(a+h))/2;*/ //Simpson's rule

    double h=(b-a)/N; //Composite Simpson's rule
    double I=0;
    double n;
    for (n=0; n<N; n++)
    {
       I=I+(h/3)*(funcion(a+(h*n))+4*funcion(a+(h*n)+h/2)+funcion(a+h+h*n))/2;
    }
     printf("\nAnswer is: %g\n", I);
     return 0;
}

int main(){
parameters();
return 0;
}
