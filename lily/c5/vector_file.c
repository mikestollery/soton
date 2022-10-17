/*
 *  vector_file.c
 *
 * Creates a vector from data read from a file
 *
 * To compile:
 *
 * gcc -c vector.c
 * gcc vector_file.c vector.o -o vector_file
 *     
 */

#include <stdio.h>
#include <stdlib.h>
#include "vector.h"

int main(int argc, char *argv[])
{    
    Vector v = createVectorFromFile("vectors.txt");
        
    printVector(v);
    destroyVector(v);
}


