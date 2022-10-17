# include <stdio.h>
#include <ctype.h>

int main () {

  FILE *fp;

  fp = fopen("text.txt", "r");

  char c = fgetc(fp);
  char u = toupper(c);

  while(c != EOF) {
    printf("%c", u);
    c = fgetc(fp);
    u = toupper(c);
  }
  fclose(fp);
}

