#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int fibonacci (int N){  //Finds the nth fibonacci number
long int a=1;
long int b=1;
int c=1;
long int n;
if (N<1) {  //If the input number is not a positive integer
  printf("The Fibonacci %i doesn't exist\n", N);
}
else {
if (c==N){ //If N=1
printf("\nThe first Fibonacci number is 1\n");
}
else {
while(c<N){
n=a+b;
a=b;
b=n;
c++;
}
printf("\nThe %ith fibonacci number is: %li\n", N, a);
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
