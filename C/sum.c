#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double sum (){
double a;
double b;
printf("Enter a number: ");
scanf("%lf", &a);
printf("\nEnter another number: ");
scanf("%lf", &b);
printf("\nThe sum is: %g\n", a+b);
return 0;
}

int main(){
sum();
return 0;
}
