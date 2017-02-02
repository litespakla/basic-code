#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <unistd.h>

static int dice(){ //In this program you enter a number of the dice and a number of rounds
  int n;
  int i;
  double c=0;
  int N;
  int L;
srand(time(NULL) + getpid());

printf("Number of the dice (1 to 6): ");
scanf("%i", &N);

printf("\nHow many rounds? ");
scanf("%i", &L);

for (i=0; i<L; i++){  //It keeps throwing the dice until it gets the number entered
  while(n!=N){
  n=rand()%6+1;
  c++;
    //printf("%i ", n); prints the throws of each round
}
  //printf("\n");
  n=0;
}
  printf("\nIt throws the dice %g times per round\n", c/i);
return 0;
}

int main(void){
dice();
return 0;
}
