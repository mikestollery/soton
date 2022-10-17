
#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <unistd.h>

void display(const uint8_t*);
void rotate(const uint8_t*);
int isBitSet(const uint8_t byte, const unsigned int pos);

int main () 
{

  // Initialise bits for each segment

  /*
    Segment        a        b        c        d        e        f        g
    Pin            7        6        5        4        3        2        1
    Bit            6        5        4        3        2        1        0
    Decimal       64       32       16        8        4        2        1
    Hex           40       20       10        8        4        2        1
    Binary  01000000 00100000 00010000 00001000 00000100 00000010 00000001

    e.g. to display 4, switch on segments b, c, f, g
    (see diagram on page 1 of SC08-11GWA.pdf)

    b 6 00100000 = 32
    c 5 00010000 = 16
    f 2 00000010 =  2
    g 1 00000001 =  1
        --------
        00110011 = 51 = 0x33
  */

  // uint8_t is the same as a byte, i.e. an unsigned integer of length 8 bits [0..255]

  const uint8_t segments[10] = {
    0x7E,    // 0 => a, b, c, d, e, f    (126)
    0x30,    // 1 => b, c                 (48)
    0x6D,    // 2 => a, b, d, e, g       (109)
    0x79,    // 3 => a, b, c, d, g       (121)
    0x33,    // 4 => b, c, f, g           (51)
    0x5B,    // 5 => a, c, d, f, g        (91)
    0x5F,    // 6 => a, c, d, e, f        (95)
    0x70,    // 7 => a, b, c             (112)
    0x7F,    // 8 => a, b, c, d, e, f, g (127)
    0x7B     // 9 => a, b, c, d, f, g    (123)
  };

  printf("Initialised segments:\n");
  for (int i = 0; i < 10; i++)
  {
    printf("segment[%d]=0x%x (%d)\n", i, segments[i], segments[i]);
  }

  display(segments);
  //rotate(segments);
}



void display(const uint8_t *segments)
{
  uint8_t byte;
  uint8_t bit;

  for (int i = 0; i < 10; i++)
  {
    byte = segments[i];
    printf("Display digit %d using byte %d\n", i, byte);   

    for (int pin = 7; pin > 0; pin--)
    {
      bit = isBitSet(byte, pin - 1);
      printf("  pin %d: %d\n", pin, bit);      
    }
  } 
}


void rotate(const uint8_t *segments)
{
  uint8_t byte;
  uint8_t bit;

  unsigned int digit = 0;

  for(;;)
  {
    if (digit > 9)
    {
      digit = 0;
    }

    byte = segments[digit];
    printf("Display digit %d using byte %d\n", digit, byte);   

    for (int pin = 7; pin > 0; pin--)
    {
      bit = isBitSet(byte, pin - 1);
      printf("  pin %d: %d\n", pin, bit);      
    }

    sleep(1);
    digit++;
  }
}


// returns 1 if bit at position pos is set, otherwise 0

int isBitSet(const uint8_t byte, const unsigned int pos)
{
    return ((byte & (1 << pos))? 1 : 0);
}


