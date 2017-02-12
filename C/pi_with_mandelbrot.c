#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*Based on this video: https://www.youtube.com/watch?v=d0vY0CKYhPY&list=PLt5AfwLFPxWJ8GCgpFo5_OSyfl7j0nOiu&index=3 */

double funcion (double z, double e){ //Function seen in the video
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
while(m<=2){ //Number of steps the algorithm lasts to surpass 2
       m=funcion(m,e);
       a=a+1;
}
while (10<a) { //Divides the number to make it less than 10
      a=a/10;
}
         printf("Pi is %g aproximately \n",a);
return 0;
}

int main(){
mandelbrot();
return 0;
}
