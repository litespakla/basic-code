#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *inputString(FILE* fp, size_t size){ //Inputs a string from terminal
//The size is extended by the input with the value of the provisional
    char *str;
    int ch;
    size_t len = 0;
    str = realloc(NULL, sizeof(char)*size);//size is start size
    if(!str)return str;
    while(EOF!=(ch=fgetc(fp)) && ch != '\n'){
        str[len++]=ch;
        if(len==size){
            str = realloc(str, sizeof(char)*(size+=16));
            if(!str)return str;
        }}
    str[len++]='\0';
    return realloc(str, sizeof(char)*len);
}

void permutations(char *conjunto, size_t card, size_t elem){ //Permutes the elements of the string
   if (card > 1){
      int i;
      permutations(conjunto, card - 1, elem + 1);
      for (i = 1; i < card; i++){
         char temp;
         temp = conjunto[elem + i];
         memmove(conjunto + elem + 1, conjunto + elem, i);
         conjunto[elem] = temp;
         permutations(conjunto, card - 1, elem + 1);
         memmove(conjunto + elem, conjunto + elem + 1, i);
         conjunto[elem + i] = temp;
      }}
      else
      puts(conjunto);
}

int main(void){
char *m;
int e;
printf("Input string :");
m = inputString(stdin, 10);
e=strlen(m);
printf("Lenght of the string is: %i\n", e);
printf("Permutations of the string are:\n");
permutations(m, e, 0);
free (m);
return 0;
}
