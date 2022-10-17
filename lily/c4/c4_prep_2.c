# include <stdio.h>

// fn changes value of x by reference
void fn(int& x) {
  x = 23;
}

int main () {

  int x = 5;
  printf("%d\n", x);
  fn(x);
  printf("%d\n", x);
}

