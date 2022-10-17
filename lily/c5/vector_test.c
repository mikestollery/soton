/*
 *  vector_test.c
 *
 * For testing fixes to vector
 *
 * To compile:
 *
 * gcc -c vector.c
 * gcc vector_test.c vector.o -o vector_test
 *     
 */

#include <stdio.h>
#include <stdlib.h>
#include "vector.h"

int main(int argc, char *argv[])
{    
    Vector v = createVector(5); // create vector of 5 elements
        
    // populate first two elements
    v.element[0] = 27;    
    v.element[1] = 42;
        
    printVector(v);
    destroyVector(v);
}


