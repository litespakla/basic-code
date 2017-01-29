#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int eratos (int N){
int sieve [N+1];  //Defines the sieve
int i;
int j;
for (i=2; i<=N; i++){
sieve[i]=i;
}
i=2;

for (i=2; i<=N; i++){  //The sieve algorithm to eliminate all non-prime numbers

  if (sieve[i]!=0){

    for (j=1; j<=N-i; j++){

      if(sieve[i+j]!=0){

         if((sieve[i+j] % sieve[i])==0){
         sieve[i+j]=0;
}}}}}
i=2;

printf("\nPrimes until %i are:\n\n", N); //Print the prime numbers
for (i=2; i<=N; i++){

  if(sieve[i]!=0){
printf("%d\n", sieve [i]);
}}

return 0;
}

int thenes (){
int N;
printf("To what natural number do you want the sieve to go: "); //Define to what number the sieve goes
scanf("%i", &N);
eratos(N);
return 0;
}

int main (void){
thenes();
return 0;
}
