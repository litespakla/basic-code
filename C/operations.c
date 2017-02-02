#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int static operations(int n){
  double a;
  double b;
  printf("\nEnter a number a: ");
  scanf("%lf", &a);
  printf("\nEnter another number b: ");
  scanf("%lf", &b);

  switch (n) {
    case 0:
    printf("\nThe sum is: %g", a+b);
    printf("\nThe rest is: %g", a-b);
    printf("\nThe multiplication is: %g", a*b);
    printf("\nThe division is: %g", a/b);
    if (ceil(a)-a==0 & ceil(b)-b==0){
      int j=ceil(a);
      int k=ceil(b);
      printf("\nThe residue of %g module %g is: %i\n",a, b, j%k);
    }
    break;
    case 1:
    printf("\nThe sum is: %g\n", a+b);
    break;
    case 2:
    printf("\nThe rest is: %g\n", a-b);
    break;
    case 3:
    printf("\nThe multiplication is: %g\n", a*b);
    break;
    case 4:
    printf("\nThe division is: %g\n", a/b);
    break;
  case 5:
  if (ceil(a)-a==0 & ceil(b)-b==0){
    int j=ceil(a);
    int k=ceil(b);
      printf("\nThe residue of %g module %g is: %i\n",a, b, j%k);
  }
  else{
    printf("\nLos números no son enteros\n");
  }
    break;
  }
  return 0;
}

int numbers(){
  int c;
  printf("This code performs all arithmetic operations.\nFor sum press 1\nFor rest press 2\nFor multiplication press 3\nFor division press 4\nTo find residue press 5\nTo perform all operations press 0:\n");
  scanf("%i", &c);
  operations(c);
  return 0;
}

int main(void){
numbers();
  return 0;
}
