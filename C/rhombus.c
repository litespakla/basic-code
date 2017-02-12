#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int static spaces (int n, int N){ //Prints the required amount of spaces for each file
  int k;
  for (k=1; k<=N-n; k++){
    printf(" ");
  }
  return 0;
}

int static rhombus (int N){
int i;
int j;
/*int N;
printf("Size of the rhombus?: ");
scanf("%i", &N);*/
for (i=1; i<=N; i++){ //Prints the upper part of the rhombus
  spaces(i, N);
  for (j=1; j<=i; j++){
    printf("* ");
  }
  printf("\n");
}

for (i=N-1; 1<=i; i=i-1){ //Prints the bottom part of the rhombus
  spaces(i, N);
  for (j=i; 1<=j; j=j-1){
    printf("* ");
  }
  printf("\n");
}
return 0;
}

int main(int argc, char *argv[]) {
rhombus(atoi(argv[1]));
  return 0;
}
