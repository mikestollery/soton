/*
 *  matrix_test.c
 *
 * For testing fixes to matrix
 *
 * To compile:
 *
 * gcc -c matrix.c
 * gcc matrix_test.c matrix.o -o matrix_test
 *     
 */

#include <stdio.h>
#include <stdlib.h>
#include "matrix.h"

int main(int argc, char *argv[])
{                
    Matrix m = createMatrix(2, 3); // create 2 x 3 matrix
            
    // add two rows to matrix
    m.element[0][0] = 1;           
    m.element[0][1] = 2;       
    m.element[0][2] = 3;       
    m.element[1][0] = 4;       
    m.element[1][1] = 5;       
    m.element[1][2] = 6;      
     
    printMatrix(m);    
    destroyMatrix(m);
}


