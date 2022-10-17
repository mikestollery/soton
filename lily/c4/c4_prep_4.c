# include <stdio.h>

int main () {

  FILE *fp;

  fp = fopen("c4_prep_4.txt", "r");

  char c = fgetc(fp);
  while(c != EOF) {
    printf("%c", c);
    c = fgetc(fp);
  }
  fclose(fp);
}

