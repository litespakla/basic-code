#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <unistd.h>

#define PI acos(-1.0)

static int pi (){
int N;     //Number of matches
double L;  //Lenght of the matches
int i=0;
double r=0;
srand(time(NULL) + getpid());

printf("How many needles?: ");
scanf("%i", &N);

printf("Lenght of the needles?: ");
scanf("%lf", &L);

  while(i<N){ //Simulates the experiment of Buffon's needles to aproximate Pi

    double p=((float)rand()/(float)(RAND_MAX))*L;
    double a=((float)rand()/(float)(RAND_MAX))*PI/2;
    double x=L*sin(a)/2;
    i++;
      if (2*L<x+p || p-x<0 ){
        r=r+1;
  }}
  printf("Pi is %g aproximately\n",N/r);
  return 0;
  }

int main(void){
pi();
return 0;
}
