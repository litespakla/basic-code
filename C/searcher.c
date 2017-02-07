#include<stdio.h>

int static secondBiggest(int *arr, int size){
   static int i;
   int j=arr[0];
   if (size==1){
     printf("You only input one number. There's no second biggest number\n");
   }
   else{
   for (i=1; i<size; i++){
   j=biggest(j, arr[i]);
 }
 for (i=0; i<size; i++){
   if (arr[i]==j){
     arr[i]=-10000000;
   }
 }
 j=-10000000;
 for (i=0; i<size; i++){
 j=biggest(j, arr[i]);
}
   printf("The second biggest element is %i\n", j);
 }
   return 0;
}

int printer (int *s, int size){
static int i;
static int j;
for (i=1; i<size; i++){
  if (s[i]!=-10000000){
    for (j=i+1; j<size; j++){
      if(s[i]==s[j]){
        s[j]=-10000000;
      }
    }
  }
}
  printf("\nNon-repeated elements of the array are: ");
for (i=0; i<size; i++){
  if(s[i]!=-10000000){
printf("%i ", s[i]);
}}
  printf("\n");
return 0;
}

int search (int *z, int size, int B){
int static i;
  printf("\nThe number are located in the positions: ");
  for (i=0; i<size; i++){
    if(z[i]==B){
      printf("Array[%i]", i+1);
    }
  }
  printf("\n");
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
  int B;
  printf("Enter %i numbers\n", n);
  for(i=0; i<n; i++)
  {
     scanf("%d", &a[i]);
  }
  printf("\nWhat number do you want to find?: ");
  scanf("%i", &B);
secondBiggest(a, n);
printer(a, n);
search(a, n, B);
return 0;
}

int main(){
  array();
return 0;
}
