# include <stdio.h>
# include <math.h>

int add(int x, int y)
{
  int z;
  z = x + y;
  return z;
}

double mysine(double x)
{
  double s = sin(x); /* range -1 to +1 */
  double y = s / 2 + 0.5;

  return y; /* range 0 to 1 */
}

void plotval(double x)
{
  double s = sin(x); /* range -1 to +1 */
  double y = s / 2 + 0.5;

}


int main () {

  /* Prep 1 */

  unsigned long int z; /* declaration */
  z = 0; /* initialisation */

  z = 27; /* assign a value */

  printf("%d\n", z); /* print out */

  /* Prep 2 */

  int a = 42;
  float b = 3.7457;

  printf("%8d\n", a); /* display integer using field width 8 chars */
  printf("%8.3f\n", b); /* display float in field width 8 chars to 3 d.p. */

  /* Prep 3 */

  while(0)
  {                                    /* endless loop */
    printf("This never ends.\n");
  }

  /* Prep 4 */

  double x = 0.5;
  double y = mysine(x);
  printf("x=%f y=%f\n", x, y);

  printf("end\n");
}

  /* double i; double s; int k = 2; int l = 3; int m; m = add(k, l); printf("%d + %d = %d\n", k, l, m); */
