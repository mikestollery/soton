/*
 *         File: circuit.h
 *       Author: Steve Gunn
 *      License: MIT License
 *         Date: 27th October 2018
 *  Description: Data structures and interfaces for modified nodal analysis of a circuit containing 
 *               voltage sources, current sources and resistors.
 */

#ifndef _CIRCUIT_H
#define _CIRCUIT_H

#include "vector.h"
#include "matrix.h"

/* Data Structures */

typedef enum {
/* TODO */
} CompType;

typedef struct {
/* TODO */
} Component;

typedef struct {
/* TODO */
} Circuit;

/* Interfaces */

Circuit createCircuitFromFile(const char *filename);
void destroyCircuit(Circuit c);
void analyseCircuit(const Circuit c);
Vector solveLinearSystem(Matrix A, Vector b);

#endif
