#include <stdio.h>
#include <ctype.h>

void calculateHistogram (char *filename, char letter_count[26]);

int main () {

    char* filename = "c4file.txt";
    char letter_count[26];

    calculateHistogram(filename, letter_count);

    printf("Letter count: \n");

    char letter;
    for (int i=0; i<26; i++) {
        letter = i + 65;
        printf("%d %c %d\n", i, letter, letter_count[i]);
    }
		
}

void calculateHistogram (char *filename, char letter_count[26]) {

    int charval;

    for (int i=0; i<26; i++) {
        letter_count[i] = 0;
    }

    FILE *fp;
    fp = fopen(filename, "r");
    char c = fgetc(fp);
    char upper = toupper(c);

    while(c != EOF) {
		
        upper = toupper(c);

        charval = upper - 65;

        if ((charval >= 0) && (charval <= 26)) {
            letter_count[charval]++;
        }

        printf("%d %c\n", charval, upper);
			 
        c = fgetc(fp); // read next character

    }

    fclose(fp);
}
	 
