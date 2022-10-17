// evol.c
// ELEC1201 Lab C3: Operators and Arrays
// Evolutionary Computing
// KPZ 2018, MIT License
//
// Compile with math library:
//    gcc evol.c -lm -o evol


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>

#define EQUATION   y = pow(x,3) - 4
#define Y_TARGET   0.0
#define EPSILON    0.0001

#define POP_SIZE     100
#define MAX_GEN    10000

#define MUTATION_STRENGTH  0.1
#define RND_INIT          42 



void printheader(void);
float rnd(); // Random values 0.0 to 1.0
void initpop(float *pop, int size);
void offspring(float parent, float mutst, float *pop, int size);

int main(){
    float population[POP_SIZE];
    int   gen = 0;
    float best_ifit = FLT_MAX;  // worst possible
    float best;
    float x, y;
    float ifit;   // inverse fitness
    int i;

    printheader();
    srand(RND_INIT);
    initpop(population, POP_SIZE);

    /* Stop iterating when best_fit falls below EPSILON */
    /* or number of generations exceeds it maximum */

    while( (gen < MAX_GEN) && (best_ifit > EPSILON)) {

        for(i=0; i < POP_SIZE; i++){
            x = population[i];

            EQUATION;  // y = f(x)

            ifit = fabs(y - Y_TARGET);

            printf("x= %f  =>  y=  %+f,    ifit = %f\n", x, y, ifit);

            // Is there a better one?
            if( ifit < best_ifit ){
                best_ifit = ifit;
                best = x;
            }
        }
        x = best;
        EQUATION;  // y = f(x)

        printf("Generation %4d with best solution:  x= %f --> f(x)= %f\n\n",
                   gen++, best, y);

        offspring( best, MUTATION_STRENGTH, population, POP_SIZE);
    }
}



void printheader(){
    printf("\n\n");
    printf("###############\n");
    printf("## Evolution ##\n");
    printf("###############\n");
}


// Returns a random value between 0.0 and 1.0
float rnd(){
    return rand()/(float) RAND_MAX;
}


void initpop(float *pop, int size) {
    /* initialise population with random numbers between 0 and 1 */

    for(int i=0; i < POP_SIZE; i++) {
        pop[i] = rnd();
        printf("pop[%d]=%f\n", i, pop[i]);
    }
}



void offspring(float parent, float mutst, float *pop, int size) {
    float mutation = 0.0;

    pop[0] = parent; /* store best solution at head of population array */

    for(int i=1; i < size; i++) { /* for rest of population vary the solution by a random amount */
        mutation = mutst * rnd();
        if (rnd() > 0.5) { /* either add or subtract this mutation to the parent */
            pop[i] = parent + mutation;
        }
        else {
            pop[i] = parent - mutation;
        }
    }
}



