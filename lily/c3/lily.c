
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

#define EQUATION   y = pow(x,4) - 8
#define Y_TARGET   0.0
#define EPSILON    0.0001

#define POP_SIZE     100
#define MAX_GEN    1000

#define MUTATION_STRENGTH  0.1
#define RND_INIT		30



/* void printheader(void);*/
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
	float fit;
	
		
	


    /* printheader(); */
    srand(RND_INIT);
    initpop(population, POP_SIZE);

	for (int rnd_init = 0; rnd_init < 10; rnd_init++) {
	
		int gen = 0; /* resets gen count for every seed */
		srand(rnd_init);
		initpop(population, POP_SIZE);
		
	
		while( (best_ifit > EPSILON) && (gen < MAX_GEN) ){

			for(i=0; i < POP_SIZE; i++){
				x = population[i];

				EQUATION;  // y = f(x)

				ifit = fabs(y - Y_TARGET);

				/* printf("x= %f  =>  y=  %+f,    ifit = %f\n", x, y, ifit); */

				// Is there a better one?
				if( ifit < best_ifit ){
					best_ifit = ifit;
					best = x;
				}
			}
			x = best;
			EQUATION;  // y = f(x)
			
			if ( best_ifit > 0 ) {
				fit = 1 / best_ifit;
			}
			else {
				fit = -1 ; 
			}

			printf("rnd_init=%d gen=%d, fit=%f \n",
					   rnd_init, gen++, fit);

			offspring( best, MUTATION_STRENGTH, population, POP_SIZE);
			
		}
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
	for( int i=0; i < size; i++) { /* i will increase by 1 each time until it is greater than POP_SIZE */
		pop [i] = rnd(); /* i is assigned random values */
	}
}

void offspring(float parent, float mutst, float *pop, int size) {
	float mutation = 0.0;
	
	pop [0] = parent; /* this stores the best value of pop [i] to pop [0] */
	
	for (int i=1; i < size ; i++) { /* this is for the rest of the population that isnt the best */
			mutation = mutst * rnd () ; /* this creates a random value of which the rest of the population is going to mutate by */
		if ( rnd() > 0.5 ) { /* for half of the population add mutation and the other half subtract mutation */
			pop [i] = parent + mutation;
		}
		else {
			pop [i] = parent - mutation;
		}
	}
}

