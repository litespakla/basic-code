#include<stdio.h>

int secondBiggest(int *arr, int size){
   static int i;
   int j=arr[0];
   int k=arr[1];
   if (size>2){
   for (i=2; i<size; i++){
   j=biggest(j, arr[i]);
   k=biggest(k, arr[i]);
 }}
 k=biggest(j, k);
   printf("The second biggest element is %i\n", j);
   return 0;
}

int biggest(int a, int b){
if (a<b){
  return b;
}
else {
  return a;
}}

int array (){
  int n;
  printf("\nLenght of the array?: ");
  scanf("%i", &n);
  int a[n];
  int i;
  int N;
  printf("Enter %i numbers\n", n);
  for(i=0; i<n; i++)
  {
     scanf("%d", &a[i]);
  }
secondBiggest(a, n);
return 0;
}

int main(){
  array();
return 0;
}
