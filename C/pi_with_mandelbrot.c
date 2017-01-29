#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double funcion (double z, double e){
double c=0.25+e;
double x=pow(z,2)+c;
return x;
}

double mandelbrot (){
double e;
printf("Enter a very tiny value: ");
scanf("%lf", &e);
double a=0.0;
double m=0.0;
while(m<=2){
       m=funcion(m,e);
       a=a+1;
       }
       while (10<a) {
         a=a/10;
              }
         printf("Pi is %g aproximately \n",a);
return 0;
}

int main(){
mandelbrot();
return 0;
}
