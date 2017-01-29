#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int fibonacci (int N){
int a=1;
int b=1;
int c=1;
int n;
if (N<1) {
  printf("The Fibonacci %i doesn't exist\n", N);
}
else {
if (c==N){
printf("\nThe first Fibonacci number is 1\n");
}
else {
while(c<N){
n=a+b;
a=b;
b=n;
c++;
}
printf("\nThe %ith fibonacci number is: %i\n", N, a);
}
return 0;
}}

int nFibonacci(){
int N;
printf("What Fibonacci N do you want to know?: ");
scanf("%i", &N);
fibonacci (N);
return 0;
}

int main(){
nFibonacci();
return 0;
}
