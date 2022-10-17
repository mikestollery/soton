#include <stdio.h>
#include <ctype.h>

void calculateHistogram (char *filename, char letter_count[26]);
void show_letter_count (const char letter_count[26]);
int max_letter_count(const char letter_count[26]);
void display_histogram(const char letter_count[26]);

int main () {

    char* filename = "c4file.txt";
    char letter_count[26];

    calculateHistogram(filename, letter_count);

    show_letter_count(letter_count);

    display_histogram(letter_count);
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

        c = fgetc(fp); // read next character
    }

    fclose(fp);
}
	 
void show_letter_count (const char letter_count[26]) {

    char letter;
    for (int i=0; i<26; i++) {
        letter = i + 65;
        printf("%d %c %d\n", i, letter, letter_count[i]);
    }
}

int max_letter_count(const char letter_count[26])
{
    int max = 0;
    for (int i=0; i<26; i++) {
        if (letter_count[i] > max) {
            max = letter_count[i];
        }
    }
    return max;
}

void display_histogram(const char letter_count[26])
{
    int max = max_letter_count(letter_count);

    char letter;
    int length = 0;
    int count = 0;
    int j;

    for (int i=0; i<26; i++) {
        letter = i + 65;
        count = letter_count[i];
        length = 80 * count / max;
        printf("%c ", letter);
       
        for (j=0; j<length; j++) {
            printf("*");
        } 
        printf("\n");
    }
}
