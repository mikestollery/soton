#include <stdio.h>
#include <ctype.h>

void calculateHistogram (char filename, char [26] alphabet);

int main () {
	void calculateHistogram (char filename, char [26] alphabet) {
		
		FILE *fp;
		fp = fopen("c4file.txt", "r");
		 char c = fgetc(fp);
		 while(c != EOF) {
		    printf("%c", toupper(c));
			 
			
			  c = fgetc(fp);
		 }
		  int charval;
		   charval = c - 65;
		    printf ("%d",charval);
	 
			  
	  
	
	}
	 
	

  fclose(fp);

}

