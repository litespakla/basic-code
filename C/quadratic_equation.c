#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int quadratic (double a, double b, double c);

int solution(){ //Input the coefficients of the equation
double a;
double b;
double c;
printf("The equation is Ax^2 + Bx + C\n\nEnter the coefficient A of the equation: ");
scanf("%lf", &a);
printf("\nEnter the coefficient B of the equation: ");
scanf("%lf", &b);
printf("\nEnter the coefficient C of the equation: ");
scanf("%lf", &c);
quadratic(a, b, c);
return 0;
}

int quadratic (double a, double b, double c){
double d;
double e;
d=pow(b,2)-4*a*c; //Determinant of the equation
if (d<0){
printf("\nEquation has no real roots\n");
}

else{ //Solutions of the equation
    e=(-b+sqrt(d))/(2*a);
    d=(-b-sqrt(d))/(2*a);
    printf("\nThe roots of the quadratic equation are:\nX1 = %g\nX2 = %g\n", e, d);
}
return 0;
}

int main (void){
solution();
return 0;
}
