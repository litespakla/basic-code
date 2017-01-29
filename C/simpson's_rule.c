#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define a 2.0  //Integration interval (a,b)
#define b 10.0
#define N 50.0  // N subintervals

double funcion (double x) //function
{
    double f=(exp(-0.3*x)*cos(4+x))/(log(x)); //Write function here
    return (f);
}

integral () //Integral with Simpson's rule
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
     printf("Answer is: %g", I);
}

main()
{
    printf("Integration interval: [%g,%g]", a, b);
    printf("\n");

    integral();
}
