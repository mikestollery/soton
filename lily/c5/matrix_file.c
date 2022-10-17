/*
 *  matrix_file.c
 *
 * Creates a matrix from data read from a file
 *
 * To compile:
 *
 * gcc -c matrix.c
 * gcc matrix_file.c matrix.o -o matrix_file
 *     
 */

#include <stdio.h>
#include <stdlib.h>
#include "matrix.h"

int main(int argc, char *argv[])
{    
    Matrix m = createMatrixFromFile("matrix.txt");
        
    printMatrix(m);
    destroyMatrix(m);
}


