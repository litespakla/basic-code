#include<stdio.h>

/*Arrays are of the type int. Only works for numbers greater than -2000000000 */

int static biggest(int *a, int size){ //Finds and return the biggest element of an array
 int b=a[0];
 int i;
  for (i=1; i<size; i++){
    if (a[i]>b){
      b=a[i];
    }}
return b;
}

int static secondBiggest(int *a, int size){ //Finds and prints the second biggest element of an array
   if (size==1){
     printf("You only input one number. There's no second biggest number\n");
   }
   else{
     int i;
     int b=biggest(a, size);
   for (i=0; i<size; i++){
   if (a[i]==b){
     a[i]=-2000000000;
   }}
b=biggest(a, size);
 printf("The second biggest element is: %i\n", b);
 }
   return 0;
}

int static printer (int *a, int size){ //Prints non-repeated elements of the array
 int i;
 int j;
 printf("Non-repeated elements of the array are: ");
 for (i=0; i<size; i++){
   if (a[i]!=-2000000000){
   for (j=0; j<size; j++){
     if (a[i]==a[j+1] & i!=j+1){
       a[j+1]=-2000000000;
     }}
   printf("%i ", a[i]);
 }}
 printf("\n");
  return 0;
}

int static searcher (int *a, int size, int B){  //Finds all the positions of the array with a specified number
int i;
  printf("The number %i is located in the array's positions: ", B);
  for (i=0; i<size; i++){
    if(a[i]==B){
      printf("%i", i+1);
      printf(", ");
    }
  }
  printf("\n");
  return 0;
}

int static array (){ //Input an array and know stuff about it
  int n;
  printf("\nLenght of the array?: ");
  scanf("%i", &n);
  if (n<1){
    printf("\nThe array has no elements\n");
  }
  else {
  int a[n];
  int i;
  int N;
  int B;
  printf("Enter %i numbers\n", n);
  for(i=0; i<n; i++)
  {
     scanf("%d", &a[i]);
  }
  printf("\nWhat number do you want to find?: ");
  scanf("%i", &B);
searcher (a, n, B);
printer(a, n);
i=biggest(a, n);
printf("The biggest element of the array is: %i\n", i);
secondBiggest(a, n);
}
return 0;
}

int main(){
  array();
return 0;
}
