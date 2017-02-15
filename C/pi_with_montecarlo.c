#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <unistd.h>

#define PI acos(-1.0)

int rdtsc()
{
    __asm__ __volatile__("rdtsc");
}

static double hits (int N, double L){
  int i=0;
  double r=0;
  srand(time(NULL) + getpid() + rdtsc());
  while(i<N){ //Simulates the experiment of Buffon's needles to aproximate Pi

    double p=((float)rand()/(float)(RAND_MAX))*2*L;
    double a=((float)rand()/(float)(RAND_MAX))*PI;
    double x=L*sin(a)/2;
    i++;
      if (2*L<x+p || p-x<0 ){
        r=r+1;
  }}
  return r;
}

int pi (){
int N, T, j;
double L, k;
long double R=0;

printf("How many needles?: "); //Number of matches
scanf("%i", &N);

printf("Lenght of the needles?: "); //Lenght of the matches
scanf("%lf", &L);

printf("How many times do you want to run the experiment: "); //Number of trials
scanf("%i", &T);

for (j=0; j<T; j++){
  k=hits(N, L);
  //printf("Result of trial %i is: %g\n", j+1, N/k);
  R+=N/k;
}
  printf("Pi is %Lf aproximately\n",R/T);
  return 0;
  }

int main(void){
pi();
return 0;
}
